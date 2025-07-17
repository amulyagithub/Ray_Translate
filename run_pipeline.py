import os
from src.tts_generate import generate_audio
from src.merge_video import merge_video_audio_subs

def run_translation_pipeline(video_path, translated_text, subtitle_path, output_video_path, audio_output_path="output/translated_audio.wav"):
    print("🎤 Generating audio from translated text...")
    generate_audio(translated_text, audio_output_path)

    if not os.path.exists(audio_output_path) or os.path.getsize(audio_output_path) < 1000:
        raise ValueError(f"Generated audio is invalid: {audio_output_path}")

    print("🎬 Merging video, audio, and subtitles...")

    
    output_directory = os.path.dirname(output_video_path)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        merge_video_audio_subs(video_path, audio_output_path, subtitle_path, output_video_path)
        print(f"✅ Final output video saved to {output_video_path}")
    except Exception as e:
        print(f"❌ Failed to merge video: {e}")
        raise e
    return output_video_path