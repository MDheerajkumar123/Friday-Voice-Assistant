'''import pyttsx3

# Initialize TTS engine only once
engine = pyttsx3.init()

# Optional: Configure voice, speed, volume
engine.setProperty('rate', 150)      # Speed (default ~200)
engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)

# You can choose a different voice if needed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # [0] for male, [1] for female (varies by OS)

def speak(text):
    print(f"🧠 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()'''

#for Mobile
'''from gtts import gTTS
import io
import pygame

def speak(text):
    print(f"🧠 Assistant: {text}")
    try:
        # Generate TTS audio in memory
        tts = gTTS(text)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Initialize pygame mixer and play from buffer
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_fp, 'mp3')
        pygame.mixer.music.play()

        # Wait until playback finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")'''

# text_output.py
from gtts import gTTS
import io

def generate_tts_audio(text: str) -> bytes:
    print(f"🧠 Assistant: {text}")
    try:
        # Generate speech audio in memory
        tts = gTTS(text)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return mp3_fp.read()  # return raw bytes
    except Exception as e:
        print(f"❌ TTS error: {e}")
        return b""




