# from translatepy import Translator
# import pysrt
# from src.emotion_detector import detect_emotion
# import re

# def translate_subtitles(srt_file_path, target_language):
#     translator = Translator()
#     subs = pysrt.open(srt_file_path)

#     for sub in subs:
#         translated_text = translator.translate(sub.text, target_language).result
#         emotion = detect_emotion(translated_text)
        
#         # Only add emotion label if it's not neutral
#         if emotion != "neutral":
#             sub.text = f"[{emotion.capitalize()}] {translated_text}"
#         else:
#             sub.text = translated_text

#     translated_srt_path = "output/translated_subs.srt"
#     subs.save(translated_srt_path)
#     return translated_srt_path

# def save_subtitles(transcription_text, output_file_path):
#     subs = pysrt.SubRipFile()
#     lines = transcription_text.split('. ')
    
#     for i, line in enumerate(lines):
#         stripped_line = line.strip()
#         if not stripped_line:
#             continue

#         emotion = detect_emotion(stripped_line)
#         if emotion != "neutral":
#             line_with_emotion = f"[{emotion.upper()}] {stripped_line}"
#         else:
#             line_with_emotion = stripped_line

#         sub = pysrt.SubRipItem(
#             i + 1,
#             start=pysrt.SubRipTime(seconds=i * 5),
#             end=pysrt.SubRipTime(seconds=(i + 1) * 5),
#             text=line_with_emotion
#         )
#         subs.append(sub)

#     subs.save(output_file_path)

# def extract_clean_text(srt_path):
#     subs = pysrt.open(srt_path)
#     clean_lines = []

#     for sub in subs:
#         # Remove [Emotion] tags
#         line = re.sub(r'\[.*?\]', '', sub.text).strip()
#         if line:
#             clean_lines.append(line)

#     return ' '.join(clean_lines)






from translatepy import Translator
import pysrt
from src.emotion_detector import detect_emotion
import re


emotion_emoji = {
    "cheerful": "😊",
    "sad": "😢",
    "angry": "😡",
    "excited": "😆",
    "fearful": "😨",
    "friendly": "🙂",
    "neutral": "😐"  
}

def translate_subtitles(srt_file_path, target_language):
    translator = Translator()
    subs = pysrt.open(srt_file_path)

    for sub in subs:
        translated_text = translator.translate(sub.text, target_language).result
        emotion = detect_emotion(translated_text)
        
        
        emoji = emotion_emoji.get(emotion, "😐")  
        if emotion != "neutral":
            sub.text = f"[{emotion.capitalize()}] {emoji} {translated_text}"
        else:
            sub.text = translated_text

    translated_srt_path = "output/translated_subs.srt"
    subs.save(translated_srt_path)
    return translated_srt_path

def save_subtitles(transcription_text, output_file_path):
    subs = pysrt.SubRipFile()
    lines = transcription_text.split('. ')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if not stripped_line:
            continue

        emotion = detect_emotion(stripped_line)
        emoji = emotion_emoji.get(emotion, "😐")  
        
        if emotion != "neutral":
            line_with_emotion = f"[{emotion.upper()}] {emoji} {stripped_line}"
        else:
            line_with_emotion = stripped_line

        sub = pysrt.SubRipItem(
            i + 1,
            start=pysrt.SubRipTime(seconds=i * 10),
            end=pysrt.SubRipTime(seconds=(i + 1) * 10-0.1),
            text=line_with_emotion
        )
        subs.append(sub)

    subs.save(output_file_path)

def extract_clean_text(srt_path):
    subs = pysrt.open(srt_path)
    clean_lines = []

    for sub in subs:
        
        line = re.sub(r'\[.*?\]', '', sub.text).strip()
        if line:
            clean_lines.append(line)

    return ' '.join(clean_lines)



