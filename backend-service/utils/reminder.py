'''import time
import threading
from utils.text_output import speak

def set_reminder(task, delay):
    def reminder_thread():
        time.sleep(delay)
        speak(f"⏰ Reminder: {task}")
    threading.Thread(target=reminder_thread).start()'''

#for Mobile
'''import time
import threading
from utils.text_output import speak

def set_reminder(task: str, delay: float):
    """
    Set a reminder to speak a task after a given delay (in seconds).
    
    Args:
        task (str): The task to remind the user about.
        delay (float): Delay in seconds before the reminder triggers.
    """
    def reminder_thread():
        try:
            time.sleep(delay)
            speak(f"⏰ Reminder: {task}")
        except Exception as e:
            print("[ERROR - Reminder Thread]:", e)
            speak("Sorry, there was a problem with your reminder.")
    
    threading.Thread(target=reminder_thread, daemon=True).start()'''

import time
import threading
from utils.text_output import generate_tts_audio

reminders = []

def set_reminder(task: str, delay: float, callback=None):
    """
    Set a reminder to generate TTS for a task after delay (in seconds).
    Optionally provide a callback to return the audio buffer.
    """
    def reminder_thread():
        try:
            time.sleep(delay)
            tts_audio = generate_tts_audio(f"⏰ Reminder: {task}")
            if callback:
                callback(tts_audio, task)
        except Exception as e:
            print("[ERROR - Reminder Thread]:", e)
    
    threading.Thread(target=reminder_thread, daemon=True).start()


