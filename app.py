from flask import Flask, request, jsonify, render_template
import os
import ffmpeg
from src.transcribe import transcribe_audio
from src.tts_generate import generate_audio
from src.translate_subs import translate_subtitles, save_subtitles, extract_clean_text
from src.merge_video import merge_video_audio_subs

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'output/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_audio_from_video(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    try:
        ffmpeg.input(video_path).output(audio_path).overwrite_output().run()
    except ffmpeg.Error as e:
        print(f"❌ FFmpeg failed during audio extraction: {e}")
        raise e
    return audio_path

def text_to_speech(text, voice_name):
    speech_path = os.path.join(OUTPUT_FOLDER, 'translated_audio.mp3')
    try:
        generate_audio(text, speech_path, voice=voice_name)
    except Exception as e:
        print(f"❌ Error during TTS: {e}")
        raise e
    return speech_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return jsonify({"error": "No video part in the request"}), 400

    file = request.files['video']
    voice_name = request.form['language']  

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = file.filename
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_path)

        audio_path = extract_audio_from_video(video_path)
        transcribed_text = transcribe_audio(audio_path)

        srt_file_path = os.path.join(OUTPUT_FOLDER, 'transcription_subs.srt')
        save_subtitles(transcribed_text, srt_file_path)

        translated_srt_path = translate_subtitles(srt_file_path, voice_name[:2])
        cleaned_text_for_speech = extract_clean_text(translated_srt_path)

        audio_file_path = text_to_speech(cleaned_text_for_speech, voice_name)

        final_video_path = os.path.join(OUTPUT_FOLDER, 'final_video.mp4')
        merge_video_audio_subs(video_path, audio_file_path, translated_srt_path, final_video_path)

        return jsonify({
            "message": "File uploaded and processed!",
            "final_video": final_video_path,
            "translated_subtitles": translated_srt_path
        }), 200

    return jsonify({"error": "Invalid file type. Only MP4 videos are allowed."}), 400

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)

