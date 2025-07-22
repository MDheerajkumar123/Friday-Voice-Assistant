# Use a lightweight official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for audio processing and gTTS
RUN apt-get update && apt-get install -y \
    build-essential \
    portaudio19-dev \
    libasound2-dev \
    libffi-dev \
    libssl-dev \
    ffmpeg \
    mpg123 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install PyAudio (must be built with PortAudio support)
RUN pip install --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir pyaudio==0.2.13

# Copy project files into container
COPY . .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install pywhatkit==5.4

# Expose the FastAPI app port
EXPOSE 7860

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
