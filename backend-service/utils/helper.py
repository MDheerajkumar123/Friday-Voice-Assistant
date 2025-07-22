import os
import re
import requests
import geocoder
from base64 import b64encode
from utils.text_output import generate_tts_audio

# 🔑 Securely get API keys from the environment variables provided by Hugging Face
GNEWS_API_KEY = os.environ.get("GNEWS_API_KEY")
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")

def audio_entry(text: str):
    """Helper to create uniform response objects."""
    return {
        "text": text,
        "audio": b64encode(generate_tts_audio(text)).decode("utf-8")
    }

def get_news():
    """Fetches top news headlines from India and returns a list of dict responses."""
    if not GNEWS_API_KEY:
        return [audio_entry("News API key is not configured in Hugging Face secrets.")]
        
    responses = [audio_entry("Fetching the latest news from India...")]
    url = f"https://gnews.io/api/v4/top-headlines?lang=en&country=in&max=5&token={GNEWS_API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        articles = data.get("articles", [])
        if not articles:
            responses.append(audio_entry("Sorry, I couldn't fetch any news right now."))
            return responses
        for idx, article in enumerate(articles, 1):
            title = article.get("title", "No title")
            responses.append(audio_entry(f"News {idx}: {title}"))
    except Exception as e:
        print("[ERROR - News Fetching]:", e)
        responses.append(audio_entry("There was an error while fetching the news."))
    return responses

def get_weather(command_text=None):
    """Gets weather info and returns a list of dict responses."""
    if not OPENWEATHER_API_KEY:
        return [audio_entry("Weather API key is not configured in Hugging Face secrets.")]

    responses = []
    city = None
    if command_text:
        match = re.search(r"in\s+([a-zA-Z\s]+)", command_text)
        if match:
            city = match.group(1).strip()
    if not city:
        location = geocoder.ip("me")
        city = location.city
    if not city:
        responses.append(audio_entry("Sorry, I couldn't detect your location."))
        return responses
    responses.append(audio_entry(f"Getting weather report for {city}..."))
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("cod") != 200:
            responses.append(audio_entry("Sorry, I couldn't find the weather for that location."))
            return responses
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        responses.append(audio_entry(f"The temperature in {city} is {temp}°C with {desc}."))
        responses.append(audio_entry(f"Humidity is {humidity}% and wind speed is {wind_speed} meters per second."))
    except Exception as e:
        print("[ERROR - Weather Fetching]:", e)
        responses.append(audio_entry("There was an error fetching the weather data."))
    return responses




