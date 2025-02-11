import os
from gtts import gTTS

def convert_text_to_speech(text, engine='google_tts'):
    if engine != 'google_tts':
        return {"error": "Unsupported engine"}

    tts = gTTS(text=text, lang='en')
    audio_path = "output.mp3"
    tts.save(audio_path)
    return audio_path
