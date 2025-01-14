import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's command
def listen():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
            return None

# Function to execute basic commands
def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "what is the time" in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "play music" in command:
        os.system("start music.mp3")  # Make sure you have an mp3 file in the same directory or provide the full path
        speak("Playing music")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()

# Main loop
speak("Hello! I am your voice assistant.")
while True:
    command = listen()
    if command:
        execute_command(command)
