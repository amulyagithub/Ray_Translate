# src/utils/generate_srt.py

def generate_srt_from_text(text, output_path='subtitles/translated_subs.srt', duration_per_line=3):
    lines = [line.strip() for line in text.strip().split('.') if line.strip()]
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, sentence in enumerate(lines):
            start = format_time(i * duration_per_line)
            end = format_time((i + 1) * duration_per_line)
            f.write(f"{i + 1}\n{start} --> {end}\n{sentence}.\n\n")

def format_time(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{int(hrs):02}:{int(mins):02}:{int(secs):02},000"
