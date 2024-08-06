import os
import speech_recognition as sr

def speak(audio):
    os.system(f'say "{audio}"')

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")  # Announce that Nemesis is listening
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Understanding..")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query  # Return the recognized query
    except Exception as e:
        print("Say that again")
        return "None"

def greet_nemesis():
    speak("Hello! I am Nemesis, your virtual assistant. How can I assist you today?")




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

        else:
            speak("Sorry, I didn't understand that.")
