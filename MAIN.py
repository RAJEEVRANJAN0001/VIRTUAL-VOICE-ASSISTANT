
import datetime
import ecapture as ec
from bs4 import BeautifulSoup
import pyautogui
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
import wikipedia
from datetime import datetime
from calculator_module import perform_calculator_operation, retrieve_history, perform_advanced_calculations
from news import fetch_news
from authentication import authenticate, change_password
import requests
from ipl_score import notify_ipl_score
from game import game_play
from playlist_player import play_playlist
from todo_manager import add_to_do, view_to_do
from utilities import takeCommand
from utilities import speak
import time
from googletrans import Translator

def greetnemesis():
    speak("Hello! I am Nemesis, your virtual assistant. How can I assist you today?")

def respond_to_compliment():
    speak("Thank you! I'm here to help and make your day easier.")

def respond_to_insult():
    speak("I'm sorry if I've upset you. My goal is to assist and provide information. How can I make things better?")
def respond_to_time_query():
    current_time = datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}.")


NEWS_API_KEY = "a0e7243221fd4fc5bd414013288b8526"  # Your News API key

def speak_news(news_headlines):
    speak("Fetching the news headlines. Please wait.")
    for headline in news_headlines:
        speak(headline)




def run_camera():
    try:
        # Assuming cam_real_time.py is in the same directory as this script
        script_path = os.path.join(os.path.dirname(__file__), "cam_real_time.py")
        process = subprocess.Popen(["python", script_path])
        speak("Camera is now running")
        return process

    except Exception as e:
        speak("Error running camera")
        return None

# Initialize process variable outside of any function
process = None


def parse_time_string(time_str):
    # Convert time string to datetime object
    try:
        return datetime.strptime(time_str, "%I:%M %p")
    except ValueError:
        pass
    try:
        return datetime.strptime(time_str, "%I %p")
    except ValueError:
        pass
    try:
        return datetime.strptime(time_str, "%H:%M")
    except ValueError:
        pass
    raise ValueError("Unrecognized time format")

def get_temperature(location):
    search = f"temperature in {location}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"The current temperature in {location} is {temp}")

def get_weather_report(location):
    api_key = "YA577CLViXPXXPkGmCvJ5Ui3DCDjtoE7"
    forecast_url = f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey={api_key}"
    realtime_url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"

    try:
        # Fetch forecast data
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        # Fetch realtime data
        realtime_response = requests.get(realtime_url)
        realtime_data = realtime_response.json()

        # Debug prints
        print("Forecast data:", forecast_data)
        print("Realtime data:", realtime_data)

        # Extract relevant weather information
        forecast_summary = forecast_data.get("forecast", {}).get("daily", [])
        realtime_summary = realtime_data.get("data", {}).get("weather", {}).get("description")

        if forecast_summary:
            forecast_summary = forecast_summary[0].get("weather", {}).get("description")
        else:
            forecast_summary = "No forecast available"

        return f"Forecast: {forecast_summary}. Realtime: {realtime_summary}"
    except Exception as e:
        print("Error fetching weather:", e)
        return "error"


def open_browser_and_search(query, browser):
    options = webdriver.ChromeOptions() if browser == 'chrome' else webdriver.ChromeOptions()
    options.binary_location = f"/Applications/{browser.capitalize()} Browser.app/Contents/MacOS/{browser.capitalize()} Browser"
    driver = webdriver.Chrome(options=options, service=ChromeService())
    try:
        search_url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query} in {browser.capitalize()} browser.")
        driver.get(search_url)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.tF2Cxc')))
    finally:
        speak(f"Do you want to close {browser.capitalize()}? Say yes to close.")
        close_browser_command = takeCommand().lower()
        if "yes" in close_browser_command:
            pyautogui.hotkey('command', 'q')
            speak(f"{browser.capitalize()} browser is now closed.")
        else:
            speak("Browser window will remain open. You can close it manually.")

def open_youtube():
    speak("Opening YouTube.")
    webbrowser.open("https://www.youtube.com")

def open_browser(browser):
    speak(f"Opening {browser.capitalize()} browser.")
    subprocess.run(["open", "-a", f"{browser.capitalize()} Browser"])

def open_new_tab(browser):
    speak(f"Opening a new tab in {browser.capitalize()} browser.")
    subprocess.run(["open", "-na", f"{browser.capitalize()} Browser", "--args", "--new-tab"])

def play_first_youtube_video(video_query):
    search_url = f"https://www.youtube.com/results?search_query={video_query}"
    speak(f"Searching YouTube for {video_query}.")
    webbrowser.open(search_url)
    time.sleep(5)
    video_thumbnail_x = 500
    video_thumbnail_y = 300
    pyautogui.click(x=video_thumbnail_x, y=video_thumbnail_y)

def select_video_on_display(video_number):
    speak(f"Selecting video number {video_number} on display.")

def pause_youtube_video():
    speak("Pausing the YouTube video.")

def resume_youtube_video():
    speak("Resuming the YouTube video.")

def stop_youtube_video():
    speak("Stopping the YouTube video.")

def searchwikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "").strip()
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia...")
    print(results)
    speak(results)

def search_and_display_webpage(search_query):
    options = webdriver.SafariOptions()
    try:
        driver = webdriver.Safari(options=options)
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query + Keys.RETURN)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        links = driver.find_elements(By.CSS_SELECTOR, "h3")
        if links:
            links[0].click()
        else:
            speak("No search results found.")
    except Exception as e:
        speak("There was an error opening the webpage.")
        print(e)

def open_google():
    speak("Opening Google.")
    subprocess.run(["open", "https://www.google.com"])

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    speak(f"Searching Google for {query}.")
    subprocess.run(["open", search_url])

def open_youtube_function(function):
    function_url_map = {
        "home": "https://www.youtube.com/",
        "trending": "https://www.youtube.com/feed/trending",
        "subscriptions": "https://www.youtube.com/feed/subscriptions",
        "library": "https://www.youtube.com/feed/library",
        "history": "https://www.youtube.com/feed/history",
        "watch later": "https://www.youtube.com/playlist?list=WL",
    }
    if function.lower() in function_url_map:
        function_url = function_url_map[function.lower()]
        speak(f"Opening YouTube {function.capitalize()} function.")
        subprocess.run(["open", function_url])
    else:
        speak("I'm sorry, I didn't recognize that YouTube function.")

def play_music():
    if os.name == 'posix':
        os.system("osascript -e 'tell app \"Music\" to play'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.play()"])

def pause_music():
    if os.name == 'posix':
        os.system("osascript -e 'tell app \"Music\" to pause'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.pause()"])

def next_track():
    if os.name == 'posix':
        os.system("osascript -e 'tell app \"Music\" to next track'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.next()"])

def previous_track():
    if os.name == 'posix':
        os.system("osascript -e 'tell app \"Music\" to previous track'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.previous()"])

def volume_up():
    if os.name == 'posix':
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "$wmp = New-Object -ComObject WMPlayer.OCX; $wmp.settings.volume += 10"])

def volume_down():
    if os.name == 'posix':
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
    elif os.name == 'nt':
        subprocess.run(["powershell", "$wmp = New-Object -ComObject WMPlayer.OCX; $wmp.settings.volume -= 10"])

def move_cursor_to_area(x, y, width, height):
    screen_width, screen_height = pyautogui.size()
    x = int((x / 100) * screen_width)
    y = int((y / 100) * screen_height)
    width = int((width / 100) * screen_width)
    height = int((height / 100) * screen_height)
    pyautogui.moveTo(x, y, duration=0.5)

def move_cursor_by_offset(x_offset, y_offset):
    current_x, current_y = pyautogui.position()
    new_x = current_x + x_offset
    new_y = current_y + y_offset
    pyautogui.moveTo(new_x, new_y, duration=0.5)

def click_at_cursor():
    pyautogui.click()
def change_cursor_speed(speed_factor):
    pyautogui.PAUSE = pyautogui.PAUSE / speed_factor

def speak_to_search_on_google():
    speak("Please speak your command to search on Google.")

def type_and_search_on_google(search_query):
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query + Keys.RETURN)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        links = driver.find_elements(By.CSS_SELECTOR, "h3")
        if links:
            links[0].click()
        else:
            speak("No search results found.")
    except Exception as e:
        speak("There was an error opening the webpage.")
        print(e)

import subprocess
import platform

def shutdown_system():
    try:
        # Check if running on macOS
        if platform.system() != 'Darwin':
            raise OSError("This function is only supported on macOS.")

        # 1. Speak Notification
        speak("Hold On a Sec! Your system is on its way to shut down")

        # 2. Execute AppleScript command to shut down the system
        script = 'tell application "System Events" to shut down'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)

        if result.returncode != 0:
            # Error occurred, print error message
            error_message = result.stderr.strip() if result.stderr else "Unknown error"
            raise RuntimeError(f"Error shutting down the system: {error_message}")

        # 3. Feedback
        speak("Your system is shutting down now. Goodbye!")

    except PermissionError:
        # Handle permission error
        speak("Sorry, I don't have the necessary permissions to shut down the system. Please run the script with elevated privileges.")
    except OSError as e:
        # Handle unsupported platform error
        speak(str(e))
    except Exception as e:
        # Handle any other exceptions
        speak(f"Sorry, I encountered an error while shutting down the system: {str(e)}")
def empty_trash():
    try:
        # 1. Speak Notification
        speak("Emptying the trash")

        # 2. Execute AppleScript command to empty the Trash
        script = 'tell application "Finder" to empty trash'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        if result.returncode == 0:
            # 3. Feedback
            speak("Trash emptied successfully.")
        else:
            # Error occurred, print error message
            error_message = result.stderr.strip() if result.stderr else "Unknown error"
            speak(f"Error emptying the trash: {error_message}")
    except Exception as e:
        # Handle any other exceptions that might occur
        speak("Sorry, I encountered an error while emptying the trash. Please try again later.")

def lock_screen():
    try:
        # Check if running on macOS
        if platform.system() != 'Darwin':
            raise OSError("This function is only supported on macOS.")

        # Prompt the user for confirmation
        speak("Are you sure you want to lock the screen?")
        confirmation = takeCommand().lower()  # Assuming takeCommand() is a function that listens for user input

        if "do it" in confirmation:
            # Lock the screen
            speak("Locking the screen now.")
            result = subprocess.run(['pmset', 'displaysleepnow'], capture_output=True, text=True)

            if result.returncode != 0:
                # Error occurred, print error message
                error_message = result.stderr.strip() if result.stderr else "Unknown error"
                raise RuntimeError(f"Error locking the screen: {error_message}")

        else:
            speak("Okay, I won't lock the screen.")

    except PermissionError:
        # Handle permission error
        speak("Sorry, I don't have the necessary permissions to lock the screen. Please run the script with elevated privileges.")
    except OSError as e:
        # Handle unsupported platform error
        speak(str(e))
    except Exception as e:
        # Handle any other exceptions
        speak(f"Sorry, I encountered an error while locking the screen: {str(e)}")
def get_bbc_news():
    # Function to fetch and display top news from BBC News
    try:
        # 1. Construct API URL
        api_key = "a0e7243221fd4fc5bd414013288b8526"
        main_url = "https://newsapi.org/v1/articles"
        source = "bbc-news"
        sort_by = "top"
        api_url = f"{main_url}?source={source}&sortBy={sort_by}&apiKey={api_key}"

        # 2. Make API Request
        response = requests.get(api_url)

        # 3. Parse JSON Response
        data = response.json()

        # 4. Extract News Articles
        articles = data["articles"]

        # 5. Display and Speak News Titles
        for i, article in enumerate(articles, 1):
            title = article['title']
            print(f"{i}. {title}")
            speak(title)  # Speak out the news title
    except Exception as e:
        # Handle any errors that might occur during the process
        print(f"Error: {e}")

# Global variable to store the music player subprocess
music_player = None

def play_n_music(music_file):
    global music_player
    try:
        # If music is already playing, terminate the previous playback
        stop_n_music()

        # Start playing the new music file
        music_player = subprocess.Popen(["afplay", music_file])
    except Exception as e:
        print(f"Error playing music: {e}")

def stop_n_music():
    global music_player
    try:
        # If music is playing, terminate the playback
        if music_player and music_player.poll() is None:
            music_player.terminate()
            music_player.wait()
    except Exception as e:
        print(f"Error stopping music: {e}")

def resume_n_music():
    global music_player
    try:
        # If music was previously stopped, resume playback
        if music_player and music_player.poll() is not None:
            music_file = "/Users/rajeevranjanpratapsingh/PycharmProjects/voise_assistent/Manike Mage Hithe (Pagalworld.pw)/01 Manike Mage Hithe (Pagalworld.pw).mp3"
    except Exception as e:
        print(f"Error resuming music: {e}")


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


import os
from pathlib import Path
import shutil

# Define the file formats and their corresponding directories
FILE_FORMATS = {
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    '.doc': 'Documents',
    '.jpg': 'Images',
    '.png': 'Images',
    '.xlsx': 'Spreadsheets',
    '.mp3': 'Audio',
    '.mp4': 'Videos',
    '.zip': 'Archives',
    '.exe': 'Executables'

}

def organize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            shutil.move(file_path, directory_path)  # Move the file to the corresponding directory
    try:
        os.mkdir("OTHER")
    except FileExistsError:
        pass
    for file in os.listdir():
        try:
            if os.path.isdir(file):
                os.rmdir(file)
            else:
                shutil.move(file, "OTHER/" + file)  # Move the remaining files to the 'OTHER' directory
        except:
            pass


if __name__ == "__main__":

    authenticated = authenticate()
    if not authenticated:
        exit()


    while True:
        query = takeCommand().lower()
        if "nemesis" in query:
            greetnemesis()
            while True:
                query = takeCommand().lower()
                print("Recognized command:", query)
                if "sleep" in query:
                    speak("Okay, you can wake me up anytime. Going to sleep now.")
                    break
                elif "how are you" in query:
                    speak("I'm doing well, thank you for asking!")
                elif "what is your name" in query:
                    speak("You can call me Nemesis.")
                elif "tell a joke" in query:
                    speak("Why did the computer go to therapy? It had too many bytes of emotional baggage!  if it was not to your liking then there  a other one is - What did the policeman say to his hungry stomach? “Freeze. You’re under a vest.What did the policeman say to his hungry stomach? “Freeze. You’re under a vest.””")
                elif 'what is' in query:
                    searchwikipedia(query)
                elif 'search on google' in query:
                    search_query = query.replace("search on google", "").strip()
                    search_google(query)
                elif 'good bye' in query:
                    speak("Goodbye!")
                    break
                elif "open youtube" in query:
                    open_youtube()

                elif "open brave browser" in query:
                    open_browser_and_search(query, 'brave')

                elif "open chrome" in query:
                    open_browser_and_search(query, 'chrome')

                elif "search on google" in query:
                    search_query = query.replace("search on google", "")
                    search_google(search_query)
                elif "open new tab in chrome" in query:
                    open_new_tab('chrome')
                elif "open new tab in brave" in query:
                    open_new_tab('brave')
                elif "open youtube function" in query:
                    function = query.replace("open youtube function", "")
                    open_youtube_function(function)
                elif "play youtube video" in query:
                    video_query = query.replace("play youtube video", "")
                    play_first_youtube_video(video_query)
                elif "pause youtube video" in query:
                    pause_youtube_video()
                elif "resume youtube video" in query:
                    resume_youtube_video()
                elif "stop youtube video" in query:
                    stop_youtube_video()

                elif "good job" in query:
                    respond_to_compliment()
                elif "you're useless" in query:
                    respond_to_insult()
                elif "what's the time" in query:
                    respond_to_time_query()

                elif "open calculator" in query:
                    perform_calculator_operation()
                elif "retrieve history" in query:
                    retrieve_history()
                elif "perform advanced calculations" in query:
                    perform_advanced_calculations()

                elif "pause music" in query:
                    pause_music()
                elif "next track" in query:
                    next_track()
                elif "previous track" in query:
                    previous_track()
                elif "volume up" in query:
                    volume_up()
                elif "volume down" in query:
                    volume_down()
                elif "move cursor to area" in query:
                    _, x, y, width, height = query.split()
                    move_cursor_to_area(int(x), int(y), int(width), int(height))
                elif "move cursor by offset" in query:
                    _, x_offset, y_offset = query.split()
                    move_cursor_by_offset(int(x_offset), int(y_offset))
                elif "single click" in query:
                    click_at_cursor()
                elif "double click" in query:
                    time.sleep(0)
                    pyautogui.doubleClick()
                    speak("Performed a double click at the current cursor position.")
                elif "right click " in query:
                    pyautogui.rightClick()
                elif "scroll up" in query:
                    pyautogui.scroll(10)
                elif "scroll down" in query:
                    pyautogui.scroll(-10)
                elif "go to top left corner" in query:
                    pyautogui.moveTo(0, 0, duration=0.5)
                elif "go to bottom right corner" in query:
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(screen_width, screen_height, duration=0.5)
                elif "capture screen" in query:
                    speak("Sure! Please specify a name for the screenshot.")
                    screenshot_name = takeCommand().lower()
                    if screenshot_name:
                        screenshot = pyautogui.screenshot()
                        screenshot.save(f"{screenshot_name}.png")
                        speak(f"The screenshot has been saved as {screenshot_name}.png.")
                    else:
                        speak("Sorry, I didn't catch the screenshot name. Please try again.")
                elif "open task manager" in query:
                    if os.name == 'posix':
                        os.system("open -a Activity Monitor")
                    elif os.name == 'nt':
                        os.system("taskmgr")
                elif "go to center" in query:
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=0.5)
                    speak("Cursor has been moved to the center of the screen.")
                elif "click and hold" in query:
                    speak("Please specify the duration for clicking and holding in seconds.")
                    duration = float(takeCommand())
                    pyautogui.mouseDown()
                    time.sleep(duration)
                    pyautogui.mouseUp()
                    speak(f"Click and hold for {duration} seconds completed.")
                elif "release click" in query:
                    pyautogui.mouseUp()
                    speak("The click has been released.")

                elif "start drawing" in query:
                    pyautogui.mouseDown()
                    speak("Drawing mode activated. You can start drawing.")

                elif "click at specific position" in query:
                    speak("Please specify the X and Y coordinates for clicking.")
                    coordinates = takeCommand().split()[-2:]
                    if len(coordinates) == 2:
                        x, y = map(int, coordinates)
                        pyautogui.moveTo(x, y, duration=0.5)
                        pyautogui.click()
                        speak(f"Clicked at position {x}, {y}.")
                    else:
                        speak("Invalid coordinates. Please provide both X and Y coordinates.")
                elif "undo last action" in query:
                    pyautogui.hotkey('ctrl', 'z') if os.name == 'posix' else pyautogui.hotkey('ctrl', 'z')
                    speak("Undo action performed.")
                elif "scroll left" in query:
                    pyautogui.hscroll(3)
                    speak("Scrolled left.")
                elif "scroll right" in query:
                    pyautogui.hscroll(-3)
                    speak("Scrolled right.")

                elif "minimize all windows" in query:
                    pyautogui.hotkey('command', 'mission_control')
                    speak("All windows have been minimized.")
                elif "restore all windows" in query:
                    pyautogui.hotkey('command', 'option', 'm')
                    speak("Restored all minimized windows.")
                elif "right click" in query:
                    pyautogui.rightClick()
                    speak("Performed a right-click.")
                elif "left click" in query:
                    pyautogui.click()
                    speak("Performed a left-click.")
                elif "double right click" in query:
                    pyautogui.rightClick()
                    pyautogui.rightClick()
                    speak("Performed a double right-click.")
                elif "double left click" in query:
                    pyautogui.doubleClick()
                    speak("Performed a double left-click at the current cursor position.")
                elif "middle click" in query:
                    pyautogui.middleClick()
                elif "double middle click" in query:
                    pyautogui.middleClick()
                    pyautogui.middleClick()
                elif "move cursor to top" in query:
                    pyautogui.moveTo(pyautogui.position()[0], 0, duration=0.5)
                elif "move cursor to bottom" in query:
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(pyautogui.position()[0], screen_height, duration=0.5)
                elif "move cursor to left" in query:
                    pyautogui.moveTo(0, pyautogui.position()[1], duration=0.5)
                elif "move cursor to right" in query:
                    screen_width, _ = pyautogui.size()
                    pyautogui.moveTo(screen_width, pyautogui.position()[1], duration=0.5)
                elif "change cursor speed" in query:
                    speed_factor = 2.0  # Adjust this value as needed
                    change_cursor_speed(speed_factor)

                elif 'search on youtube' in query:
                    query = query.replace("search on youtube", "")
                    search_url = f"https://www.youtube.com/results?search_query={query}"
                    speak(f"Searching YouTube for {query}.")
                    webbrowser.open(search_url)
                elif 'search on stack overflow' in query:
                    query = query.replace("search on stack overflow", "")
                    search_url = f"https://stackoverflow.com/search?q={query}"
                    speak(f"Searching Stack Overflow for {query}.")
                    webbrowser.open(search_url)

                elif 'search on bing' in query:
                    query = query.replace("search on bing", "")
                    search_url = f"https://www.bing.com/search?q={query}"
                    speak(f"Searching Bing for {query}.")
                    webbrowser.open(search_url)
                elif 'search on yahoo' in query:
                    query = query.replace("search on yahoo", "")
                    search_url = f"https://search.yahoo.com/search?p={query}"
                    speak(f"Searching Yahoo for {query}.")
                    webbrowser.open(search_url)

                elif 'search on ask' in query:
                    query = query.replace("search on ask", "")
                    search_url = f"https://www.ask.com/web?q={query}"
                    speak(f"Searching Ask.com for {query}.")
                    webbrowser.open(search_url)

                elif 'search on github' in query:
                    query = query.replace("search on github", "")
                    search_url = f"https://github.com/search?q={query}"
                    speak(f"Searching GitHub for {query}.")
                    webbrowser.open(search_url)
                elif 'search on reddit' in query:
                    query = query.replace("search on reddit", "")
                    search_url = f"https://www.reddit.com/search/?q={query}"
                    speak(f"Searching Reddit for {query}.")
                    webbrowser.open(search_url)
                elif 'search on quora' in query:
                    query = query.replace("search on quora", "")
                    search_url = f"https://www.quora.com/search?q={query}"
                    speak(f"Searching Quora for {query}.")
                    webbrowser.open(search_url)
                elif 'search on facebook' in query:
                    query = query.replace("search on facebook", "")
                    search_url = f"https://www.facebook.com/search/top/?q={query}"
                    speak(f"Searching Facebook for {query}.")
                    webbrowser.open(search_url)
                elif 'search on twitter' in query:
                    query = query.replace("search on twitter", "")
                    search_url = f"https://twitter.com/search?q={query}"
                    speak(f"Searching Twitter for {query}.")
                    webbrowser.open(search_url)
                elif 'search on instagram' in query:
                    query = query.replace("search on instagram", "")
                    search_url = f"https://www.instagram.com/explore/tags/{query}/"
                    speak(f"Searching Instagram for #{query}.")
                    webbrowser.open(search_url)
                elif 'search on pinterest' in query:
                    query = query.replace("search on pinterest", "")
                    search_url = f"https://www.pinterest.com/search/pins/?q={query}"
                    speak(f"Searching Pinterest for {query}.")
                    webbrowser.open(search_url)
                elif 'search on linkedin' in query:
                    query = query.replace("search on linkedin", "")
                    search_url = f"https://www.linkedin.com/search/results/all/?keywords={query}"
                    speak(f"Searching LinkedIn for {query}.")
                    webbrowser.open(search_url)
                elif 'search on snapchat' in query:
                    query = query.replace("search on snapchat", "")
                    search_url = f"https://www.snapchat.com/search?q={query}"
                    speak(f"Searching Snapchat for {query}.")
                    webbrowser.open(search_url)

                elif 'search on whatsapp' in query:
                    query = query.replace("search on whatsapp", "")
                    search_url = f"https://api.whatsapp.com/send?phone={query}"
                    speak(f"Searching WhatsApp for {query}.")
                    webbrowser.open(search_url)



                elif 'search on zoom' in query:
                    query = query.replace("search on zoom", "")
                    search_url = f"https://zoom.us/search?q={query}"
                    speak(f"Searching Zoom for {query}.")
                    webbrowser.open(search_url)
                elif 'search on teams' in query:
                    query = query.replace("search on teams", "")
                    search_url = f"https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/group-chat-software?market=en-US&rtc=1&activetab=pivot%3aoverviewtab&q={query}"
                    speak(f"Searching Microsoft Teams for {query}.")
                    webbrowser.open(search_url)


                elif 'search on slack' in query:
                    query = query.replace("search on slack", "")
                    search_url = f"https://slack.com/intl/en-sg/help/articles/218095017-Find-your-way-around-Slack#search"
                    speak(f"Searching Slack for {query}.")
                    webbrowser.open(search_url)


                elif 'search on booking' in query:
                    query = query.replace("search on booking", "")
                    search_url = f"https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AvS3ofkFwAIB&sid=29a0590486320624d6011e82e5edf982&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AvS3ofkFwAIB%3Bsid%3D29a0590486320624d6011e82e5edf982%3Bsb_price_type%3Dtotal%26%3B&ss={query}"
                    speak(f"Searching Booking.com for {query}.")
                    webbrowser.open(search_url)
                elif 'search on airbnb' in query:
                    query = query.replace("search on airbnb", "")
                    search_url = f"https://www.airbnb.com/s/{query}"
                    speak(f"Searching Airbnb for {query}.")
                    webbrowser.open(search_url)
                elif 'search on expedia' in query:
                    query = query.replace("search on expedia", "")
                    search_url = f"https://www.expedia.com/Hotel-Search?destination={query}&tab=home"
                    speak(f"Searching Expedia for {query}.")
                    webbrowser.open(search_url)


                elif "change password" in query:
                    change_password()

                elif "temperature" in query:
                    speak("Sure! Please specify the location.")
                    location = takeCommand()
                    get_temperature(location)

                elif "weather" in query:
                    speak("Sure! Please specify the location.")
                    location = takeCommand()
                    weather_report = get_weather_report(location)
                    if weather_report != "error":
                        speak(f"The weather report for {location} is {weather_report}")
                    else:
                        speak("Sorry, I couldn't fetch the weather report.")


                elif "news" in query:
                    news_headlines = fetch_news(NEWS_API_KEY)
                    speak_news(news_headlines)





                elif "play a game" in query:
                    game_play()


                elif "detect emotion" in query:
                    if process is None or process.poll() is not None:
                        process = run_camera()
                    else:
                        speak("Camera is already running.")

                elif "stop camera" in query:
                    if process and process.poll() is None:
                        process.kill()
                        speak("Camera stopped.")
                    else:
                        speak("No camera is running.")


                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "play music" in query or "play playlist" in query:
                    play_playlist("playlist.txt")  # Assuming playlist.txt contains the paths to the songs

                if "add my list to do" in query:
                    speak("What task would you like to add to your to-do list?")
                    task = takeCommand()
                    if task:
                        add_to_do(task)
                elif "view my list to do" in query:
                    view_to_do()

                elif 'lock window' in query or "system ko lock Karen" in query:
                    lock_screen()

                elif 'shutdown system' in query:
                    shutdown_system()

                elif 'empty recycle bin' in query:
                    empty_trash()

                elif "bbc news" in query:
                    get_bbc_news()

                elif"play song" in query or "gaana" in query or "song" in query:

                    speak("Sure, please provide the path to your music directory.")

                    speak("For example, it could be '/Users/your_username/Music'")

                    speak("What is the path to your music directory?")

                    music_dir = input("Path to Music directory: ").strip()  # Get the music directory path from the user

                    if os.path.isdir(music_dir):

                        songs = os.listdir(music_dir)

                        if songs:

                            speak("Playing a random song for you.")

                            random_song = os.path.join(music_dir, songs[0])

                            play_n_music(random_song)  # Play the music file

                        else:

                            speak("Sorry, I couldn't find any music files in the specified directory.")

                    else:

                        speak("Sorry, the specified directory does not exist.")


                elif 'stop music' in query or 'pause music' in query:

                    stop_n_music()

                    speak("Music playback stopped.")


                elif 'resume music' in query or 'play music' in query:

                    resume_n_music()

                    speak("Resuming music playback.")

                elif "organised files" in query:
                    organize()
                    speak("Files have been organized successfully.")

                elif "translate" in query:
                    translate_text()

                elif "exit" in query:
                    speak("Goodbye!")

                    break
                else:
                     speak("")
