cs361-voice-command-app
Version: v1.0.0

This is a Python-based voice command application that responds to specific voice commands to open popular applications like Chrome, Spotify, and Discord. Users can activate the command mode by saying "Hey Jarvis," after which the program listens for predefined commands. Users can also deactivate the assistant or close the program using voice commands.

Features
Activates upon hearing "Hey Jarvis"
Opens applications: Chrome, Spotify, and Discord
Commands: "open Chrome", "open Spotify", "open Discord"
"deactivate Jarvis" to stop command mode
"close program" to exit the program
Requirements
This application is compatible with Windows only.

Dependencies
To run this program, you need the following Python libraries installed:

os (built-in library, no installation needed)
subprocess (built-in library, no installation needed)
pygetwindow
win32gui, win32con (from the pywin32 library)
pyautogui
time (built-in library, no installation needed)
speech_recognition
pyttsx3
pyaudio (for speech_recognition library to work correctly)

Installations
pip install pygetwindow
pip install pywin32
pip install pyautogui
pip install SpeechRecognition
pip install pyttsx3

(Optional) Set up a virtual environment to keep dependencies isolated:
python -m venv env
source env/bin/activate  # Use `env\Scripts\activate` on Windows
