import whisper
import os

def transcribe_audio(video_file_path):
    
    if not os.path.exists(video_file_path):
        raise FileNotFoundError(f"Audio file {video_file_path} not found!")

    try:
        model = whisper.load_model("base")  
        audio = whisper.load_audio(video_file_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(model, mel, options)
        return result.text  # Return the transcription text
    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        raise e
