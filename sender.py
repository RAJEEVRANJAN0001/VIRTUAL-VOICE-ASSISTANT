import os
import subprocess
import time
import speech_recognition as sr
from googletrans import Translator

def speak(audio):
    os.system(f'say "{audio}"')

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Understanding..")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def greet_nemesis():
    speak("Hello! I am Nemesis, your virtual assistant. How can I assist you today?")

def translate_text():
    translator = Translator()
    speak("Sure! What text would you like to translate?")
    text = takeCommand()
    speak("Which language would you like to translate it to?")
    lang = takeCommand()
    translated_text = translator.translate(text, dest=lang)
    print(f"Translated text: {translated_text.text}")
    speak("Here is the translated text:")
    speak(translated_text.pronunciation)



if __name__ == "__main__":
    greet_nemesis()
    while True:
        query = takeCommand().lower()
        if "sleep" in query:
            speak("Okay, you can wake me up anytime. Going to sleep now.")
            break
        elif "how are you" in query:
            speak("I'm doing well, thank you for asking!")
        elif "what is your name" in query:
            speak("You can call me Nemesis.")
        elif "translate" in query:
            translate_text()
        else:
            speak("Sorry, I didn't understand that.")

