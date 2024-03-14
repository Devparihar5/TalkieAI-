from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import torch

class AudioTranscriber:
    def __init__(self, model_id="openai/whisper-tiny.en", cache_dir=r'/cache/'):
        self.processor = WhisperProcessor.from_pretrained(model_id, cache_dir=cache_dir)
        self.model = WhisperForConditionalGeneration.from_pretrained(model_id, cache_dir=cache_dir)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        
        # Model configuration
        forced_decoder_ids = self.processor.get_decoder_prompt_ids(
            language="en", task="transcribe"
        )
        self.model.config.forced_decoder_ids = forced_decoder_ids
    
    def transcribe(self, audio_content_path):
        try:
            # Converting the audio file to a waveform
            wavform, sr = librosa.load(audio_content_path, sr=16000)
            
            # Splitting the audio into segments
            segment_length = 10  # seconds
            segment_samples = segment_length * sr
            segments = [wavform[i:i+segment_samples] for i in range(0, len(wavform), segment_samples)]
            
            # Transcribing each segment
            transcriptions = []
            for segment in segments:
                input_features = self.processor(
                    segment.tolist(),
                    sampling_rate=sr,
                    return_tensors="pt",
                ).input_features

                predicted_ids = self.model.generate(input_features, forced_decoder_ids=self.model.config.forced_decoder_ids)
                transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
                transcriptions.append(transcription)
            
            return ' '.join(transcriptions)

        except Exception as error:
            print(f"Error during transcription: {str(error)}")
            return f"Server Error"
