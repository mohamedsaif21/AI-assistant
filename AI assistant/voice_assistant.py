# voice_assistant.py
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."

def respond(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen_command()
        if "exit" in command:
            respond("Goodbye!")
            break
        respond(f"You said: {command}")
