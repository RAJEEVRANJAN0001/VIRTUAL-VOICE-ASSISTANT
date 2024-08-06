import os
import speech_recognition as sr
import speech_recognition_python

import subprocess
import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import wikipedia
from datetime import datetime, time
from calculator_module import perform_calculator_operation, retrieve_history, perform_advanced_calculations
from utilities import takeCommand, speak

from news_reader import get_news

def speak(audio):
    os.system(f'say "{audio}"')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, could not understand.")
        return "."
    return query
def greetNemesis():
    speak("Hello! I am Nemesis, your virtual assistant. How can I assist you today?")
def respond_to_compliment():
    speak("Thank you! I'm here to help and make your day easier.")
def respond_to_insult():
    speak("I'm sorry if I've upset you. My goal is to assist and provide information. How can I make things better?")
def respond_to_time_query():
    current_time = datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}.")
def open_brave_and_search_google(query):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    driver = webdriver.Chrome(options=options, service=ChromeService())
    try:
        search_url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query} in Brave browser.")
        driver.get(search_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tF2Cxc')))
    finally:
        speak("Do you want to close Brave? Say yes to close.")
        close_browser_command = takeCommand().lower()
        if "yes" in close_browser_command:
            pyautogui.hotkey('command', 'q')
            speak("Brave browser is now closed.")
        else:
            speak("Browser window will remain open. You can close it manually.")
def open_chrome_and_search_google(query):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    driver = webdriver.Chrome(options=options, service=ChromeService())
    try:
        search_url = f"https://www.google.com/search?q={query}"
        speak(f"Searching Google for {query} in Chrome.")
        driver.get(search_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tF2Cxc')))
    finally:
        speak("Do you want to close Chrome? Say yes to close.")
        close_browser_command = takeCommand().lower()
        if "yes" in close_browser_command:
            pyautogui.hotkey('command', 'q')
            speak("Chrome is now closed.")
        else:
            speak("Browser window will remain open. You can close it manually.")
def open_youtube():
    speak("Opening YouTube.")
    webbrowser.open("https://www.youtube.com")
def open_brave():
    speak("Opening Brave browser.")
    subprocess.run(["open", "-a", "Brave Browser"])
def open_chrome():
    speak("Opening Google Chrome.")
    subprocess.run(["open", "-a", "Google Chrome"])
def open_new_tab_chrome():
    speak("Opening a new tab in Google Chrome.")
    subprocess.run(["open", "-na", "Google Chrome", "--args", "--new-tab"])
def open_new_tab_brave():
    speak("Opening a new tab in Brave browser.")
    subprocess.run(["open", "-na", "Brave Browser", "--args", "--new-tab"])
def play_first_youtube_video(video_query):
    search_url = f"https://www.youtube.com/results?search_query={video_query}"
    speak(f"Searching YouTube for {video_query}.")
    webbrowser.open(search_url)
    # Wait for the page to load (adjust the sleep time based on your internet speed)
    time.sleep(5)
    # Adjust the coordinates based on your screen resolution and browser layout
    # These are example coordinates; you need to find the actual coordinates
    video_thumbnail_x = 500
    video_thumbnail_y = 300
    # Simulate clicking on the first video thumbnail
    pyautogui.click(x=video_thumbnail_x, y=video_thumbnail_y)
def select_video_on_display(video_number):
    speak(f"Selecting video number {video_number} on display.")
    # Placeholder: Use pyautogui to simulate a click on the specified video on the display
    # Example: pyautogui.click(x, y)
def pause_youtube_video():
    speak("Pausing the YouTube video.")
    # Placeholder: Use keyboard library to send a pause shortcut
    # Example: keyboard.press_and_release('space')
def resume_youtube_video():
    speak("Resuming the YouTube video.")
    # Placeholder: Use keyboard library to send a play or resume shortcut
    #Example: keyboard.press_and_release('space')
def stop_youtube_video():
    speak("Stopping the YouTube video.")
    # Placeholder: Use keyboard library to send a close tab or browser shortcut
    # Example: keyboard.press_and_release('ctrl+w')
# Function to search Wikipedia
def searchWikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "").strip()
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia...")
    print(results)
    speak(results)
# Function to perform a Google search and display the first link
def search_and_display_webpage(search_query):
    options = webdriver.SafariOptions()
    try:
        driver = webdriver.Safari(options=options)
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query + Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
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
    # Play music function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'tell app \"Music\" to play'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.play()"])
def pause_music():
    # Pause music function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'tell app \"Music\" to pause'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.pause()"])
def next_track():
    # Play the next track function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'tell app \"Music\" to next track'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.next()"])
def previous_track():
    # Play the previous track function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'tell app \"Music\" to previous track'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "(New-Object -ComObject WMPlayer.OCX).controls.previous()"])
def volume_up():
    # Increase volume function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "$wmp = New-Object -ComObject WMPlayer.OCX; $wmp.settings.volume += 10"])
def volume_down():
    # Decrease volume function for different operating systems
    if os.name == 'posix':  # macOS
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
    elif os.name == 'nt':  # Windows
        subprocess.run(["powershell", "$wmp = New-Object -ComObject WMPlayer.OCX; $wmp.settings.volume -= 10"])
def move_cursor_to_area(x, y, width, height):
    # Move cursor to a specified area on the screen
    screen_width, screen_height = pyautogui.size()
    x = int((x / 100) * screen_width)
    y = int((y / 100) * screen_height)
    width = int((width / 100) * screen_width)
    height = int((height / 100) * screen_height)
    pyautogui.moveTo(x, y, duration=0.5)

def move_cursor_by_offset(x_offset, y_offset):
    # Move cursor by a specified offset
    current_x, current_y = pyautogui.position()
    new_x = current_x + x_offset
    new_y = current_y + y_offset
    pyautogui.moveTo(new_x, new_y, duration=0.5)
def click_at_cursor():
    # Click at the current cursor position
    pyautogui.click()
def speak_news(category):
    # Get news for the specified category
    articles = get_news(category)
    if articles:
        # Read out the headlines
        for idx, article in enumerate(articles[:5]):  # Read top 5 headlines
            speak(f"Headline {idx + 1}: {article['title']}")
            time.sleep(1)  # Pause between headlines
    else:
        speak("Failed to fetch news. Please try again later.")
def speak_to_search_on_google():
    speak("Please speak your command to search on Google.")
def type_and_search_on_google(search_query):
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)
    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        # Type the search query in the search bar
        search_box.send_keys(search_query + Keys.RETURN)
        # Wait for the search results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        # Click on the first link if available
        links = driver.find_elements(By.CSS_SELECTOR, "h3")
        if links:
            links[0].click()
        else:
            speak("No search results found.")
    except Exception as e:
        speak("There was an error opening the webpage.")
        print(e)

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()  # Convert the query to lowercase
        if "nemesis" in query:
            greetNemesis()
            while True:
                query = takeCommand().lower()
                print("Recognized command:", query)  # Debugging line
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
                    searchWikipedia(query)
                elif 'search on google' in query:
                    search_query = query.replace("search on google", "").strip()
                    search_google(query)
                elif 'good bye' in query:
                    speak("Goodbye!")
                    break
                elif "open youtube" in query:
                    open_youtube()

                elif "open brave browser" in query:
                    open_brave()
                    speak("Brave browser is now open. What would you like to do next?")
                    # Listen for the next command
                    query = takeCommand().lower()
                    if "play youtube video" in query:
                        # Extract the video query from the command
                        video_query = query.replace("play youtube video", "")
                        play_first_youtube_video(video_query)
                    elif "select video" in query:
                        # Extract the video number from the command
                        video_number = query.replace("select video", "")
                        select_video_on_display(video_number)
                    elif "search on brave" in query:
                        search_query = query.replace("search on brave", "")
                        open_brave_and_search_google(search_query)

                elif "open chrome" in query:
                    open_chrome()
                    speak("chrome browser is now open. What would you like to do next?")
                    # Listen for the next command
                    query = takeCommand().lower()
                    if "play youtube video" in query:
                        # Extract the video query from the command
                        video_query = query.replace("play youtube video", "")
                        play_first_youtube_video(video_query)
                    elif "select video" in query:
                        # Extract the video number from the command
                        video_number = query.replace("select video", "")
                        select_video_on_display(video_number)
                    elif "search on chrome" in query:
                        search_query = query.replace("searching ", "")
                        open_chrome_and_search_google(search_query)

                elif "search on google" in query:
                    # Extract the search query from the command
                    search_query = query.replace("search on google", "")
                    search_google(search_query)
                elif "open new tab in chrome" in query:
                    open_new_tab_chrome()
                elif "open new tab in brave" in query:
                    open_new_tab_brave()
                elif "open youtube function" in query:
                    # Extract the YouTube function from the command
                    function = query.replace("open youtube function", "")
                    open_youtube_function(function)
                elif "play youtube video" in query:
                    # Extract the video query from the command
                    video_query = query.replace("play youtube video", "")
                    play_first_youtube_video(video_query)
                elif "pause youtube video" in query:
                    pause_youtube_video()
                elif "resume youtube video" in query:
                    resume_youtube_video()
                elif "stop youtube video" in query:
                    stop_youtube_video()
                elif "weather today" in query:
                    speak("I'm sorry, I don't have real-time weather information. You can check a weather website for that.")
                elif "good job" in query:
                    respond_to_compliment()
                elif "you're useless" in query:
                    respond_to_insult()
                elif "what's the time" in query:
                    respond_to_time_query()
                elif "open the google" in query:
                    open_google()
                elif "open calculator" in query:
                    perform_calculator_operation()
                elif "retrieve history" in query:
                    retrieve_history()
                elif "perform advanced calculations" in query:
                    perform_advanced_calculations()
                elif "play music" in query:
                    play_music()
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
                    # Extracting the coordinates and dimensions from the query
                    _, x, y, width, height = query.split()
                    # Moving the cursor to the specified area on the screen
                    move_cursor_to_area(int(x), int(y), int(width), int(height))
                elif "move cursor by offset" in query:
                    # Extracting the offsets from the query
                    _, x_offset, y_offset = query.split()
                    # Moving the cursor by the specified offset
                    move_cursor_by_offset(int(x_offset), int(y_offset))
                elif "single click" in query:
                    # Performing a click at the current cursor position
                    click_at_cursor()
                elif "double click" in query:
                    time.sleep(0)
                    pyautogui.doubleClick()
                    speak("Performed a double click at the current cursor position.")
                elif "right click " in query:
                    # Performing a right-click at the current cursor position
                    pyautogui.rightClick()
                elif "scroll up" in query:
                    # Simulating scrolling up
                    pyautogui.scroll(10)
                elif "scroll down" in query:
                    # Simulating scrolling down
                    pyautogui.scroll(-10)
                elif "go to top left corner" in query:
                    # Moving the cursor to the top-left corner of the screen
                    pyautogui.moveTo(0, 0, duration=0.5)
                elif "go to bottom right corner" in query:
                    # Moving the cursor to the bottom-right corner of the screen
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(screen_width, screen_height, duration=0.5)
                elif "capture screen" in query:
                    # Command: "Capture screen"
                    speak("Sure! Please specify a name for the screenshot.")
                    # Assuming 'screenshot_name' is obtained from user's speech
                    screenshot_name = takeCommand().lower()
                    # Validate the screenshot name and save the screenshot
                    if screenshot_name:
                        # Capturing the current screen at the cursor position
                        screenshot = pyautogui.screenshot()
                        screenshot.save(f"{screenshot_name}.png")
                        speak(f"The screenshot has been saved as {screenshot_name}.png.")
                    else:
                        speak("Sorry, I didn't catch the screenshot name. Please try again.")
                elif "open task manager" in query:
                    # Opening the task manager using a system-specific command
                    if os.name == 'posix':  # macOS
                        os.system("open -a Activity Monitor")
                    elif os.name == 'nt':
                        os.system("taskmgr")
                elif "go to center" in query:
                    # Command: "Go to center"
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=0.5)
                    speak("Cursor has been moved to the center of the screen.")
                elif "click and hold" in query:
                    # Command: "Click and hold"
                    speak("Please specify the duration for clicking and holding in seconds.")
                    duration = float(takeCommand())
                    pyautogui.mouseDown()
                    time.sleep(duration)  # Wait for the specified duration
                    pyautogui.mouseUp()
                    speak(f"Click and hold for {duration} seconds completed.")
                elif "release click" in query:
                    # Command: "Release click"
                    pyautogui.mouseUp()
                    speak("The click has been released.")
                elif "toggle cursor visibility" in query:
                    # Command: "Toggle cursor visibility"
                    pyautogui.FAILSAFE = not pyautogui.FAILSAFE
                    visibility_status = "visible" if pyautogui.FAILSAFE else "invisible"
                    speak(f"The cursor is now {visibility_status}.")
                elif "start drawing" in query:
                    # Command: "Start drawing"
                    pyautogui.mouseDown()
                    speak("Drawing mode activated. You can start drawing.")
                elif "stop drawing" in query:
                    # Command: "Stop drawing"
                    pyautogui.mouseUp()
                    speak("Drawing mode deactivated.")
                elif "click at specific position" in query:
                    # Command: "Click at specific position"
                    speak("Please specify the X and Y coordinates for clicking.")
                    coordinates = takeCommand().split()[-2:]  # Extract the last two values (X and Y coordinates)
                    if len(coordinates) == 2:
                        x, y = map(int, coordinates)
                        pyautogui.moveTo(x, y, duration=0.5)
                        pyautogui.click()
                        speak(f"Clicked at position {x}, {y}.")
                    else:
                        speak("Invalid coordinates. Please provide both X and Y coordinates.")
                elif "undo last action" in query:
                    # Command: "Undo last action"
                    pyautogui.hotkey('ctrl', 'z') if os.name == 'posix' else pyautogui.hotkey('ctrl', 'z')
                    speak("Undo action performed.")
                elif "scroll left" in query:
                    # Command: "Scroll left"
                    pyautogui.hscroll(3)
                    speak("Scrolled left.")
                elif "scroll right" in query:
                    # Command: "Scroll right"
                    pyautogui.hscroll(-3)
                    speak("Scrolled right.")
                elif "switch to next window" in query:
                    # Command: "Switch to next window"
                    pyautogui.hotkey('command', 'tab')
                    speak("Switched to the next window.")
                elif "switch to previous window" in query:
                    # Command: "Switch to previous window"
                    pyautogui.hotkey('command', 'shift', 'tab')
                    speak("Switched to the previous window.")
                elif "minimize all windows" in query:
                    # Command: "Minimize all windows"
                    pyautogui.hotkey('command', 'mission_control')
                    speak("All windows have been minimized.")
                elif "restore all windows" in query:
                    # Command: "Restore all windows"
                    pyautogui.hotkey('command', 'option', 'm')
                    speak("Restored all minimized windows.")
                elif "right click" in query:
                    # Command: "Right-click"
                    pyautogui.rightClick()
                    speak("Performed a right-click.")
                elif "left click" in query:
                    # Command: "Left-click"
                    pyautogui.click()
                    speak("Performed a left-click.")
                elif "double right click" in query:
                    # Command: "Double right-click"
                    pyautogui.rightClick()
                    pyautogui.rightClick()
                    speak("Performed a double right-click.")
                elif "double left click" in query:
                    # Command: "Double left-click at the current cursor position"
                    pyautogui.doubleClick()
                    speak("Performed a double left-click at the current cursor position.")
                elif "middle click" in query:
                    # Simulating a middle click at the current cursor position
                    pyautogui.middleClick()
                elif "double middle click" in query:
                    # Simulating a double middle click at the current cursor position
                    pyautogui.middleClick()
                    pyautogui.middleClick()
                elif "move cursor to top" in query:
                    # Moving the cursor to the top of the screen
                    pyautogui.moveTo(pyautogui.position()[0], 0, duration=0.5)
                elif "move cursor to bottom" in query:
                    # Moving the cursor to the bottom of the screen
                    screen_width, screen_height = pyautogui.size()
                    pyautogui.moveTo(pyautogui.position()[0], screen_height, duration=0.5)
                elif "move cursor to left" in query:
                    # Moving the cursor to the left of the screen
                    pyautogui.moveTo(0, pyautogui.position()[1], duration=0.5)
                elif "move cursor to right" in query:
                    # Moving the cursor to the right of the screen
                    screen_width, _ = pyautogui.size()
                    pyautogui.moveTo(screen_width, pyautogui.position()[1], duration=0.5)
                elif "change cursor speed" in query:
                    # Changing the cursor speed (adjust the factor as needed)
                    speed_factor = 2.0  # Increase or decrease as needed
                    pyautogui.speed = pyautogui.speed * speed_factor
                elif "toggle drag lock" in query:
                    # Toggling the drag lock mode (hold down the mouse button after a drag operation)
                    pyautogui.dragLock()
                elif 'news' in query:
                    speak("Sure! Which category would you like to hear about?")
                    category = takeCommand().lower()
                    speak_news(category)
                elif "exit" in query or "stop" in query:
                    break
                else:
                    speak("")
