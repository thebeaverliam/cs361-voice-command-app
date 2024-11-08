import os
import subprocess
import pygetwindow as gw
import win32gui
import win32con
import pyautogui
import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_phrase():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please say something.")
        audio = recognizer.listen(source)

    try:
        phrase = recognizer.recognize_google(audio).lower()
        print(f"You said: '{phrase}'")  # Show what was said in text
        return phrase
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None

def listen_for_confirmation():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        confirmation = recognizer.recognize_google(audio).lower()
        print(f"Confirmation received: '{confirmation}'")
        return confirmation
    except sr.UnknownValueError:
        print("Confirmation not recognized. Please say 'yes' or 'no'.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None

def confirm_and_execute(app_name, execute_function):
    print(f"Are you sure you want to {app_name}? Please confirm by saying 'yes' or 'no'.")
    while True:
        confirmation = listen_for_confirmation()
        if confirmation == "yes":
            print(f"Executing: {app_name}...")
            execute_function()
            break
        elif confirmation == "no":
            print("Command canceled.")
            break
        else:
            print("Confirmation not recognized. Please say 'yes' to confirm or 'no' to cancel.")

def bring_window_to_front(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)

def open_chrome():
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def open_spotify():
    os.system("start spotify")

def open_discord():
    subprocess.Popen([
        "C:\\Users\\LiamM\\AppData\\Local\\Discord\\Update.exe",
        "--processStart", 
        "Discord.exe"
    ])
    time.sleep(5)
    try:
        discord_icon_location = pyautogui.locateCenterOnScreen('discord_icon.png', confidence=0.8)
        if discord_icon_location:
            pyautogui.click(discord_icon_location)
            print("Clicked on Discord icon.")
        else:
            print("Could not locate Discord icon on the taskbar.")
    except pyautogui.ImageNotFoundException:
        print("Could not locate the Discord icon on the screen.")

def close_program():
    print("Closing program. Goodbye!")
    exit()

def main():
    print("Program started. Voice commands enabled.")
    print("Say 'Hey Jarvis' to activate command mode.")

    command_mode = False

    while True:
        phrase = listen_for_phrase()

        if phrase:
            if not command_mode:
                speak(phrase)

                if "hey jarvis" in phrase:
                    print("Hey Jarvis detected! Now listening for commands...")
                    command_mode = True

            else:
                if "open chrome" in phrase:
                    confirm_and_execute("open Chrome", open_chrome)
                elif "open spotify" in phrase:
                    confirm_and_execute("open Spotify", open_spotify)
                elif "open discord" in phrase:
                    confirm_and_execute("open Discord", open_discord)
                elif "deactivate jarvis" in phrase:
                    print("Deactivating Jarvis. Say 'Hey Jarvis' to activate command mode again.")
                    command_mode = False
                elif "close program" in phrase:
                    confirm_and_execute("close the program", close_program)
                    return 
                else:
                    print("Command not recognized. Try saying 'open Chrome', 'open Spotify', 'open Discord', 'deactivate Jarvis', or 'close program'.")

if __name__ == "__main__":
    main()