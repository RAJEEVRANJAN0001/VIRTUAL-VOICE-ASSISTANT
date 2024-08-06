from utilities import takeCommand, speak


def authenticate():
    for i in range(3):
        speak("Please speak the password to open nemesis.")
        password = takeCommand()
        with open("password.txt", "r") as pw_file:
            stored_pw = pw_file.read().strip()

        if password == stored_pw:
            speak("Welcome, sir! Please say 'nemesis' to load me up.")
            return True
        elif i == 2:
            speak("Authentication failed. Exiting...")
            exit()
        else:
            speak("Incorrect password. Please try again.")

def change_password():
    speak("What's the new password?")
    new_pw = takeCommand()
    with open("password.txt", "w") as pw_file:
        pw_file.write(new_pw)
    speak("Password changed successfully.")
    speak(f"Your new password is {new_pw}")
