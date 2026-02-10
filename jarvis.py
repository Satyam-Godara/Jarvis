import speech_recognition as sr
import os
import subprocess
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_apps():
    speak("Good morning. Opening your workspace.")

    # Open Chrome
    subprocess.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe")

    # Open VS Code
    subprocess.Popen("C:/Users/ASUS/AppData/Local/Programs/Microsoft VS Code/Code.exe")

    # Open a folder
    os.startfile("D:/desktop")

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")

        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio).lower()
                print("You said:", text)

                if "jarvis wakeup" in text or "hello" in text:
                    open_apps()

            except:
                pass

listen()
