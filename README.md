# Friday: A Conversational Voice Assistant

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python&style=flat-square)
![Java](https://img.shields.io/badge/Java-Android-orange.svg?logo=java&style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&style=flat-square)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-f9a825?logo=huggingface&style=flat-square)
![Picovoice](https://img.shields.io/badge/Picovoice-Porcupine-6C47FF?style=flat-square)
![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-0077be?style=flat-square)
![G-News](https://img.shields.io/badge/API-G--News-34a853?style=flat-square)
![OkHttp](https://img.shields.io/badge/OkHttp-Networking-2C3E50?style=flat-square)
![Lottie](https://img.shields.io/badge/Lottie-Animations-00BFFF?style=flat-square)

> Your powerful, hands-free AI assistant for Android, powered by NLP and custom wake-word technology.

Friday is a conversational voice assistant for Android devices, combining a native Java client and a Python backend (FastAPI, Docker, Hugging Face Spaces). Friday enables real-time, natural voice interaction, smart automation (calls, reminders, apps, news, weather), and multi-modal responses—all with privacy and extensibility in mind.

---

## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Generator](#generator)
- [Badge](#badge)
- [Example Readmes](#example-readmes)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

---

## Background

This project started to create a fully open and extensible personal assistant for Android, inspired by classic AI assistants but powered by modern NLP and cloud deployment. The goal is to provide a privacy-friendly, feature-rich, and developer-friendly base for conversational AI on mobile.

---

## Install

### Backend (Hugging Face Space)

1. **Fork this repository** to your own GitHub account.
2. **Get API keys** for:
   - [OpenWeatherMap](https://openweathermap.org/) (weather)
   - [G-News](https://gnews.io/) (news)
3. **Create a Hugging Face Space**:
   - Go to your Hugging Face profile → “New Space” → Docker SDK → Blank template.
   - Link to your fork of this repo.
4. **Add secrets** in Space settings:
   ```
   GNEWS_API_KEY = your_gnews_key
   OPENWEATHER_API_KEY = your_openweathermap_key
   ```
5. **Deploy**: The Space will build and start automatically. Copy the public Space URL.

### Android App

1. **Clone your fork** and open the Android project in Android Studio.
2. **Get a free Porcupine Access Key** from [Picovoice Console](https://picovoice.ai/console/).
3. **Create a `local.properties` file** in the root of the Android project:
   ```
   HF_BACKEND_URL="https://your-username-your-space-name.hf.space/process"
   PORCUPINE_ACCESS_KEY="your_picovoice_key"
   ```
4. **Build and run** the app (sync Gradle if needed).

---

## Usage

- Say **“Hello Friday”** to activate.
- Try commands such as:
  - “Call Mom”
  - “Open YouTube”
  - “Remind me to buy groceries at 7 PM”
  - “What’s the latest news?”
  - “What’s the weather like in Nandyala?”
  - “Open https://www.google.com/search?q=Google.com”

Friday responds with both text and speech for a natural, hands-free experience.

---

## Generator

Looking to start your own standard-compliant README? Use [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme):

```sh
npx generator-standard-readme
```

---

## Badge

Show off your standard-readme compliance:

```markdown
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
```

---

## Example Readmes

- [This README itself](https://github.com/MDheerajkumar123/Friday-Voice-Assistant/blob/main/README.md)
- [standard-readme example](https://github.com/RichardLitt/standard-readme/blob/master/example-readmes/)

---

## Related Efforts

- [standard-readme](https://github.com/RichardLitt/standard-readme)
- [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme)

---

## Maintainers

- [MDheerajkumar123](https://github.com/MDheerajkumar123) - creator, lead maintainer

---

## Contributing

Contributions are welcome! Please open an issue or pull request to discuss improvements or new features. For major changes, open an issue first to discuss your proposal.

---

## License

MIT © 2025 MDheerajkumar123

See [LICENSE](LICENSE) for details.
