'''import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # wait 1 second of silence before stopping
        recognizer.energy_threshold = 300  # adjust if it's too sensitive or not sensitive enough

        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Network error.")
            return ""

#For Mobile
import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    # Optional: adjust mic for ambient noise
    with sr.Microphone() as source:
        print("🎙️ Listening... (Speak now)")
        recognizer.pause_threshold = 1  # 1s silence before cutting
        recognizer.energy_threshold = 300  # mic sensitivity threshold

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out. No speech detected.")
            return ""

        try:
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()

        except sr.UnknownValueError:
            print("❌ Sorry, I couldn't understand what you said.")
            return ""

        except sr.RequestError:
            print("⚠️ Network error: Unable to contact the speech recognition service.")
            return "" '''

# speech_input.py
import speech_recognition as sr

def transcribe_audio_file(audio_file_path: str) -> str:
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("⚠️ Network error or API issue.")
        return ""
    except Exception as e:
        print(f"❌ Error: {e}")
        return ""


