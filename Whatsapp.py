import pywhatkit
import datetime
import speech_recognition
import os
from datetime import timedelta

def speak(audio):
    os.system(f'say "{audio}"')

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.datetime.now().strftime("%H"))
update = int((datetime.datetime.now() + timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Whom do you want to message? Say 'Person one' or 'Person two'.")
    while True:
        person = takeCommand().lower()
        if "one" in person:
            speak("What's the message for Person one?")
            message = takeCommand()
            break
        elif "two" in person:
            speak("What's the message for Person two?")
            message = takeCommand()
            break
        else:
            speak("Please say 'Person one' or 'Person two'.")

    pywhatkit.sendwhatmsg("+91000000000", message, time_hour=strTime, time_min=update)

sendMessage()
