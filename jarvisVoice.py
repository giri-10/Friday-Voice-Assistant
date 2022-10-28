import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# sapi5 is a speech api from Microsoft
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet user according to the time
def greeting():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 15:
        speak("Good afternoon!!")
    elif hour >= 15 and hour < 19:
        speak("Good Evening!!")
    else:
        speak("Good Night!!")

    speak("I am Jarvis . How may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    greeting()
    
    while True:
        query = takeCommand().lower()
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open github' in query:
            webbrowser.get(chrome_path).open("github.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open photoshop' in query:
            PPath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
            os.startfile(PPath)
  
