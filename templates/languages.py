import re
from collections import defaultdict


raw_text = """(your full text here)"""


entries = re.findall(r"Name: (.*?), Locale: (.*?), Gender: (.*?)\n?", raw_text)


voices = defaultdict(lambda: {"Male": None, "Female": None})

for name, locale, gender in entries:
    if not voices[locale][gender]:
        voices[locale][gender] = name


options = []
for locale, genders in voices.items():
    for gender, name in genders.items():
        if name:
            options.append(f'<option value="{name}">{name} (Locale: {locale}, Gender: {gender})</option>')


print("\n".join(sorted(options)))
