Friday: A Conversational Voice Assistant 🤖

Meet Friday, your personal voice assistant built from the ground up, running on your Android device. More than just a simple command-follower, Friday is powered by modern NLP models and a custom wake-word engine to help you with everyday tasks, completely hands-free.

This project combines a native Android frontend with a powerful Python backend hosted on Hugging Face, creating a seamless and responsive AI experience.

✨ Key Features

Custom Wake-Word: Say "Hello Friday" to activate the assistant, powered by the highly efficient Porcupine SDK.

Real-time Voice Interaction: Have a natural, back-and-forth conversation with real-time audio processing.

Smart Task Automation:

📞 Make Calls: "Call Mom"

🚀 Launch Apps: "Open YouTube"

⏰ Set Reminders: "Remind me to buy groceries at 7 PM"

📰 Get News & Weather: "What's the latest news?" or "What's the weather like in Nandyala?"

🌐 Browse the Web: "Open https://www.google.com/search?q=Google.com"

Multi-Modal Responses: Get answers in both text and voice.

Powered by Transformers: Utilizes Hugging Face models for natural language understanding and intent recognition.

🏗️ Architecture

This project uses a modern client-server architecture to deliver a fast and intelligent experience.

Android App (Client): The native Android application continuously listens for the "Hello Friday" wake-word on-device.

API Backend (Server): Once activated, the app streams audio to a FastAPI backend hosted on Hugging Face Spaces.

NLP Processing: The backend uses Hugging Face Transformers to understand the user's intent, gathers information from external APIs (like G-News and OpenWeatherMap), and sends a structured response back.

Response: The Android app receives the response and presents it to the user through both text on the screen and a generated voice.

🛠️ Tech Stack

A look at the technologies that bring Friday to life:

Frontend (Android App)
Language: Java

IDE: Android Studio

Wake-Word Engine: Picovoice Porcupine SDK

UI: XML, Lottie for animations

Networking: OkHttp

Backend (Hugging Face Space)

Framework: FastAPI

Language: Python

NLP: Hugging Face Transformers

Deployment: Docker, Hugging Face Spaces

APIs: G-News, OpenWeatherMap

🚀 Getting Started: A Guide for Developers

This guide will walk you through deploying your own instance of the backend and connecting the Android app to it.

Part 1: Deploying the Backend

Fork this Repository: Start by forking this project to your own GitHub account.

Obtain API Keys: You'll need to get your own free API keys from the following services:

OpenWeatherMap (for weather data)

G-News (for news headlines)

Create a Hugging Face Space:

Go to your Hugging Face profile and click New Space.

Give it a name and select the Docker SDK. Choose the "Blank" template.

After creating the Space, link it to the GitHub repository you forked.

Add Secrets:

In your new Space's Settings, scroll down to Repository secrets.

Add your API keys here. This keeps them secure.

GNEWS_API_KEY = your_gnews_key_here

OPENWEATHER_API_KEY = your_openweathermap_key_here

Deploy: Your Space will automatically build and deploy. Once it's running, copy your Space's public URL (e.g., https://your-username-your-space-name.hf.space).

Part 2: Setting Up the Android App
Open the project in Android Studio from your forked repository.

Obtain Porcupine Access Key: Get your own free Access Key from the Picovoice Console.

Create local.properties file: In the root directory of the Android project, create a file named local.properties.

Add your configuration: Paste your new backend URL and your Porcupine key into this file.

Properties

# The URL of YOUR new Hugging Face Space deployment
HF_BACKEND_URL="paste_your_new_hugging_face_url_here/process"

# Your private access key from Picovoice Console
PORCUPINE_ACCESS_KEY="paste_your_picovoice_access_key_here"
Build the App: Sync Gradle and run the project. The app will now be connected to your own personal backend instance.

🙏 Acknowledgements
This project wouldn't be possible without the amazing services and tools provided by:

Hugging Face for the incredible NLP models and hosting.

Picovoice for the on-device Porcupine wake-word engine.

OpenWeatherMap and G-News for their powerful and easy-to-use APIs.
