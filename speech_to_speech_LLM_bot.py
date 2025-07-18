import speech_recognition as sr
from gtts import gTTS
import playsound
import tempfile
import ollama
import os
import threading
import cv2
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f" You said: {text}")
        return text
    except sr.UnknownValueError:
        print(" Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f" Error: {e}")
        return None

#Opens webcam in parallel in a seperate thread with the voice assistant loop.
def show_webcam():
    cap = cv2.VideoCapture(0)  # 0 = default camera
    if not cap.isOpened():
        print(" Error: Cannot access webcam")
        return

    print(" Webcam is running. Press 'q' in the video window to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Live Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def get_llm_response(prompt):
    print(" Thinking...")
    response = ollama.chat(
        model='tinyllama',  # or 'llama2' or any installed model
        messages=[
            {"role": "system", "content": "You are a friendly voice assistant. Always respond in 1 short sentence."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response['message']['content']
    print(f" LLM Response: {answer}")
    return answer



def speak_text(text):
    print("Speaking")
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  # Adjust speed here
    engine.say(text)
    engine.runAndWait()


def main():
    print(" Speech-to-Speech LLM Bot Ready!")

    # Start webcam preview
    webcam_thread = threading.Thread(target=show_webcam, daemon=True)
    webcam_thread.start()

    while True:
        text = recognize_speech()
        if text is None:
            continue
        if text.lower() in ["exit", "quit", "stop"]:
            print(" Goodbye!")
            break
        response = get_llm_response(text)
        speak_text(response)


if __name__ == "__main__":
    main()
