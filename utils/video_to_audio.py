import moviepy.editor as mp

class VideoToAudioConverter:
    def __init__(self, video_path):
        self.video_path = video_path
    
    def convert_to_audio(self, output_audio_path, codec='libvorbis'):
        try:
            # Load the video file
            video = mp.VideoFileClip(self.video_path)
            # Extract the audio from the video
            audio = video.audio
            # Write the audio to the specified output path
            audio.write_audiofile(output_audio_path, codec=codec)
            print("Audio successfully extracted from the video and saved to:", output_audio_path)
        except Exception as e:
            print("An error occurred:", str(e))

