# Ray_Translate
This project aims at translating multiple languages using AI. It is a multilingual video translation with subtitles generated in the translated language.

🎥 Translatron – Multilingual Video Translator with Emotion & Gender Matching

Translatron is an advanced multilingual video translation tool designed to automatically translate videos into multiple languages while preserving **emotions**, **timing**, and **speaker gender**. Built using Python, Flask, Whisper, TranslatePy, Edge TTS, and Gradio, this project is aimed at making cross-language video communication more human, emotional, and accessible.

🔥 Features emotional speech synthesis and **gender-matched voice output** for a natural viewer experience.


 🚀 Features

* 🎙️ **Speech Transcription** using OpenAI Whisper
* 🌍 **Automatic Translation** using TranslatePy / Argos Translate
* 🧠 **Speaker Gender Detection** for voice customization
* 😢 **Emotion-Aware Speech Generation** using Microsoft Edge-TTS
* 📼 **Re-synchronization of Audio & Subtitles** with ffmpeg
* 💻 **Gradio / Flask UI** for simple interaction and video download


🧠 Tech Stack

| Area               | Tools / Libraries                            |
| ------------------ | -------------------------------------------- |
| Backend            | Python, Flask                                |
| UI                 | Gradio (for local interface)                 |
| Translation        | TranslatePy, Argos Translate                 |
| Speech Recognition | OpenAI Whisper                               |
| Text-to-Speech     | Edge TTS with emotion + gender voice control |
| Audio Processing   | ffmpeg, pydub                                |
| Subtitle Handling  | pysrt, SRT manipulation                      |


 📂 Project Structure

Translatron/
│
├── app.py                      
├── video_processor.py         
├── templates/
│   └── index.html              
├── static/
│   └── output/                 
├── models/                     
├── README.md
└── requirements.txt
```


 🔧 How It Works

1. 🎥 Upload any video with speech.
2. 🧠 The system extracts audio and transcribes it using **Whisper**.
3. 🌐 Translated text is generated using **TranslatePy/Argos**.
4. 🕺 Emotion is inferred and speaker **gender is detected**.
5. 🗣️ Edge TTS generates **emotionally expressive, gender-matching speech**.
6. 🎞️ The new audio is synchronized back with the video using `ffmpeg`.
7. 📥 Download the fully translated video with aligned speech and subtitles.



 🌈 Key Innovations

* ✅ **Gender-aware speech output** (e.g., male speakers get male voices)
* ✅ **Emotionally expressive speech** instead of robotic monotone
* ✅ **Language-agnostic** pipeline using open-source translation models
* ✅ Built-in support for subtitle generation and editing


💻 Run Locally (Google Colab Compatible)

```bash
git clone https://github.com/yourusername/translatron
cd translatron
pip install -r requirements.txt
python app.py
```



📸 Demo Screenshot

<img width="1748" height="776" alt="image" src="https://github.com/user-attachments/assets/a39f8423-48f6-4ee9-a378-ec611f50a834" />


🧪 Future Work

* 🎚️ Fine-grained emotion control (anger, sadness, joy, etc.)
* 🧍 Multi-speaker diarization
* 🎛️ Subtitle style customization
* ☁️ Deploy to Hugging Face / Render for public access

---

 🙋‍♀️ Made With ❤️ By

**Amulya**
*“Breaking language and emotional barriers through AI-powered video translation.”*

