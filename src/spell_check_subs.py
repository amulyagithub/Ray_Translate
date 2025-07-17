import emoji
from spellchecker import SpellChecker
import pysrt


spell = SpellChecker()

def correct_spelling(text):
    """Correct spelling in the provided text"""
    words = text.split()
    corrected_words = [spell.correction(word) if word.isalpha() else word for word in words]
    return ' '.join(corrected_words)

def save_corrected_subtitles(subtitles_text, output_file_path):
    """Correct the spelling and emojis in subtitle text and save the result."""
    corrected_subtitles = []

    for subtitle in subtitles_text:
        corrected_text = correct_spelling(subtitle['text'])
        
        
        corrected_text = emoji.emojize(corrected_text)

        
        corrected_subtitles.append({
            'start_time': subtitle['start_time'],
            'end_time': subtitle['end_time'],
            'text': corrected_text
        })

    
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for subtitle in corrected_subtitles:
            f.write(f"{subtitle['start_time']} --> {subtitle['end_time']}\n")
            f.write(f"{subtitle['text']}\n\n")

    print(f"Subtitles saved to {output_file_path}")

def extract_clean_text(subtitle_file_path):
    """Extract clean text from an SRT file."""
    subs = pysrt.open(subtitle_file_path, encoding='utf-8')
    cleaned_text = []
    
    for sub in subs:
        cleaned_text.append({
            'start_time': sub.start,
            'end_time': sub.end,
            'text': sub.text
        })

    return cleaned_text
