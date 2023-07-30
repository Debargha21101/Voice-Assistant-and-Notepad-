import os
import pyttsx3
from sys import platform

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def banner():
    speak("Welcome to our project!")
    print("1. Voice Notepad\n2. Voice Assistant")
    speak("Please enter your choice:")


#banner()
text = input("Please enter your choice: ")
if text == "1" or text == "Voice Notepad" or text == "Notepad" or text == "notepad":
    if platform == "linux" or platform == "linux2":
        os.system("Linux/voicenote.py") 
    elif platform == "win32":
        os.system("Windows/voicenote.py")

elif text == "Voice Assistant" or text == "2" or text == "Assistant" or text == "assistant":
    os.system("PythonProjects.py")
else: 
    print()