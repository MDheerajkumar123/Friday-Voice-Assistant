from datetime import datetime
import re
import wikipedia
import dateparser
from base64 import b64encode
import base64
from wikipedia.exceptions import DisambiguationError, PageError
from utils.text_output import generate_tts_audio
from utils.helper import get_news, get_weather
from utils.reminder import set_reminder
from zoneinfo import ZoneInfo

def audio_response(text: str, url: str = "", app: str = ""):
    audio_bytes = generate_tts_audio(text)
    return {
        "text": text,
        "url": url,
        "app": app,
        "audio": b64encode(audio_bytes).decode("utf-8")
    }

def handle_command(command: str, payload: dict = None):
    try:
        command = command.lower()

        if "play" in command:
            command_lower = command.lower()

            if "on spotify" in command_lower:
                song = command_lower.replace("play", "").replace("on spotify", "").strip()
                spotify_url = f"https://open.spotify.com/search/{song.replace(' ', '%20')}"
                return audio_response(f"Searching for {song} on Spotify.", url=spotify_url)

            elif "on youtube" in command_lower:
                query = command_lower.replace("play", "").replace("on youtube", "").strip()
                youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                return audio_response(f"Searching for {query} on YouTube.", url=youtube_url)

            else:
                song = command.replace("play", "").strip()
                return audio_response(f"You said to play {song}, but please specify 'on Spotify' or 'on YouTube'.")

        elif "time" in command:
            india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
            time_now = india_time.strftime("%I:%M %p")
            return audio_response(f"The current time is {time_now}.")

        elif "date" in command:
            india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
            today = india_time.strftime("%A, %B %d, %Y")
            return audio_response(f"Today is {today}.")

        elif "who is" in command or "what is" in command:
            topic = command.replace("who is", "").replace("what is", "").strip()
            try:
                summary = wikipedia.summary(topic, sentences=2)
                return audio_response(summary)
            except (DisambiguationError, PageError):
                return audio_response("That topic is ambiguous or not found.")
            except Exception:
                return audio_response("Something went wrong while fetching Wikipedia info.")

        elif "open" in command:
            target = command.replace("open", "").replace("app", "").strip()
            app_name = target.lower()
            return audio_response(f"Opening {app_name} ", app=app_name)

        elif "news" in command:
            return get_news()

        elif "weather" in command:
            return get_weather(command)

        elif "remind me" in command:
            match = re.search(r"remind me to (.+?) (on|at|by) (.+)", command)
            if match:
                task = match.group(1).strip()
                datetime_str = match.group(3).strip()
                reminder_time = dateparser.parse(datetime_str)

                if reminder_time is None:
                    return audio_response("Sorry, I couldn't understand the date and time.")
                else:
                    reminder_time = reminder_time.replace(tzinfo=ZoneInfo("Asia/Kolkata"))
                    now = datetime.now(ZoneInfo("Asia/Kolkata"))
                    delay = (reminder_time - now).total_seconds()
                    if delay <= 0:
                        return audio_response("That time is already past. Please set a future reminder.")
                    else:
                        set_reminder(task, delay)
                        readable_time = reminder_time.strftime('%I:%M %p on %B %d')
                        speech = f"Okay, I will remind you to {task} at {readable_time}."
                        audio_data = generate_tts_audio(speech)

                        return {
                            "text": speech,
                            "audio": base64.b64encode(audio_data).decode("utf-8"),
                            "reminder": {
                                "task": task,
                                "timestamp": int(reminder_time.timestamp() * 1000)
                            },
                            "url": "",
                            "app": ""
                        }
            else:
                return audio_response("Please say something like 'Remind me to take medicine on May 18 at 9 AM'.")

    except Exception as e:
        print("[ERROR - handle_command]:", e)
        return audio_response("There was an error handling your request.")
