# Speech_to_Speech_LLM_Bot
This project is a Python-based speech-to-speech voice assistant that uses a local LLM (Large Language Model) for natural conversation. It captures voice input through a microphone, processes it using a pretrained language model (e.g., TinyLLaMA or LLaMA2), and responds using offline text-to-speech. A live webcam feed is also displayed during interaction.

## Features

* Converts speech to text using a microphone
* Generates intelligent responses using local LLMs via Ollama
* Converts responses to speech using offline TTS (pyttsx3)
* Displays live video from the webcam
* Achieves end-to-end latency under 3 seconds

## Libraries Used

* `speech_recognition` – for speech-to-text
* `pyttsx3` – for offline text-to-speech
* `cv2` (OpenCV) – for webcam video stream
* `ollama` – to run local LLMs like LLaMA2 or TinyLLaMA
* `threading`, `os` – for multitasking and cleanup

## Pretrained LLM Models Used

* [TinyLLaMA](https://ollama.com/library/tinyllama)
* [LLaMA2](https://ollama.com/library/llama2)

Both models are used locally via [Ollama](https://ollama.com/).

## Requirements

Install the required Python packages:

```bash
pip install speechrecognition pyttsx3 opencv-python ollama
```

Install and run a model with Ollama:

```bash
ollama pull tinyllama
```

## How to Run

```bash
python speech_to_speech_llm.py
```

* Speak into your microphone when prompted.
* Watch your webcam video in a separate window.
* The assistant will respond aloud with a short, natural reply.
* Say "exit" or "quit" to stop the assistant.
* Press `q` in the webcam window to close the video feed.

## Notes

* The entire system runs offline after pulling the model.
* You can replace `tinyllama` with any model supported by Ollama (like `llama2`, `mistral`, etc.).
* Works on Windows, Linux, and macOS.

