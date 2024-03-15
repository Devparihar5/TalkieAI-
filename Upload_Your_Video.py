import streamlit as st
from pytube import YouTube
from utils.video_to_audio import VideoToAudioConverter
from utils.transcribe import AudioTranscriber
from utils.document_processor import DocumentProcessor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# function to create pdf of transcription
def generate_pdf_report(transcription):
    output_pdf_path = "tempfiles/transcription.pdf"
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    max_width = letter[0] - 100 
    y = 750  
    for line in transcription.split('\n'):
        words = line.split()
        x = 50  
        for word in words:
            if c.stringWidth(word, "Helvetica", 12) + x > max_width:
                y -= 12 
                x = 50 
            c.drawString(x, y, word)
            x += c.stringWidth(word + " ", "Helvetica", 12)  # Move x to the end of the word
        y -= 12  
    c.save()

# setting HUGGINGFACEHUB_API_TOKEN as env variable
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

with open("style.css", "r") as file:
    custom_css = file.read()
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)


st.title("TalkieAI 📽️")

option = st.radio("Choose an option", ("Upload Video", "YouTube Link"))
output_audio_path = "temp_audio/audio.webm"
video_folder = "videos"
            
if option == "Upload Video":
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4"])
    if st.button('Upload Video'):
        if uploaded_file is not None:
            
            if not os.path.exists(video_folder):
                os.makedirs(video_folder)
            video_path = os.path.join(video_folder, "sample_video.mp4")
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.video(video_path)
        
            progress_bar = st.progress(0)

            progress_text = st.empty()
            progress_text.write("Converting video to audio...")
            converter = VideoToAudioConverter(video_path)
            converter.convert_to_audio(output_audio_path)
            progress_bar.progress(30)

            progress_text.write("Transcribing audio...")
            transcriber = AudioTranscriber()
            transcription = transcriber.transcribe(output_audio_path)
            generate_pdf_report(transcription)
            progress_bar.progress(70)
            
            progress_text.write("Training Model on Your Video...")
            document_processor = DocumentProcessor()
            updated_vector = document_processor.process_document()
            progress_text.write("100% Complete!")
            progress_bar.progress(100)
            
elif option == "YouTube Link":
    youtube_link = st.text_input("Enter YouTube Video Link:")
    if st.button("Download and Process"):
        if youtube_link:
            st.write("Downloading YouTube video...")
            try:
                yt = YouTube(youtube_link)
                video = yt.streams.get_highest_resolution()
                output_video_path = "videos"
                if os.path.exists(output_video_path):
                    items = os.listdir(output_video_path)
                    
                    for item in items:
                        item_path = os.path.join(output_video_path, item)
                        if os.path.isfile(item_path):
                            os.remove(item_path)
                
                video.download(output_video_path)
                if os.path.exists(output_video_path):
                    items = os.listdir(output_video_path)
                    
                    for item in items:
                        item_path = os.path.join(output_video_path, item)
                        if os.path.isfile(item_path) and item.lower().endswith(".mp4"):
                            os.rename(item_path, os.path.join(output_video_path, "sample_video.mp4"))
                output_video_path = output_video_path + "\sample_video.mp4"
                st.video(output_video_path)
                
                progress_bar = st.progress(0)
                progress_text = st.empty()
                progress_text.write("Converting video to audio...")
                converter = VideoToAudioConverter(output_video_path)
                converter.convert_to_audio(output_audio_path)
                progress_bar.progress(30)
                progress_text = st.empty()


                progress_text.write("Transcribing audio...")
                transcriber = AudioTranscriber()
                transcription = transcriber.transcribe(output_audio_path)
                generate_pdf_report(transcription)
                progress_bar.progress(70)
                progress_text = st.empty()
                
                progress_text.write("Processing document...")
                document_processor = DocumentProcessor()
                updated_vector = document_processor.process_document()
                progress_text.write("100% Complete!")
                progress_bar.progress(100)
            except Exception as e:
                st.error(f"Error: {str(e)}")
