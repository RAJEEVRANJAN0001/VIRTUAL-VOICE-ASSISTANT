import os
import speech_recognition

def speak(audio):
    os.system(f'say "{audio}"')

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(source, 0, 3)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def add_to_do(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    speak(f"Task '{task}' added to to-do list.")

def view_to_do():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                speak("Here are your to-do list tasks:")
                for task in tasks:
                    speak(task.strip())
            else:
                speak("Your to-do list is empty.")
    except FileNotFoundError:
        speak("Your to-do list is empty.")