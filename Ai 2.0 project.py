import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pygame  # pip install pygame
import requests 

# Initialize pygame mixer for audio control
pygame.mixer.init()

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. Mam, Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if "_name_" == "_main_":
    wishMe()
    while True:
        query = takeCommand().lower()

def playMusic(music_dir):
    songs = os.listdir(music_dir)
    if songs:
        music_path = os.path.join(music_dir, songs[0])
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        speak("Playing music.")
        print(f"Playing {music_path}")
    else:
        speak("No music files found.")

def stopMusic():
    pygame.mixer.music.stop()
    speak("Music stopped.")

def stopYoutube():
    os.system("taskkill /F /IM chrome.exe")
    speak("YouTube has been stopped.")

def openNotepad():
    os.system("notepad.exe")

def closeNotepad():
    os.system("taskkill /F /IM notepad.exe")

def openCamera():
    os.system("start microsoft.windows.camera:")

def shutdown():
    speak("Shutting down the system")
    os.system("shutdown /s /t 5")

def restart():
    speak("Restarting the system")
    os.system("shutdown /r /t 5")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            playMusic(music_dir)

        elif 'stop music' in query:
            stopMusic()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Tanu Bose\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
       
        elif 'open notepad' in query:
            openNotepad()
        elif 'close notepad' in query:
            closeNotepad()
        elif 'open camera' in query:
            openCamera()
        elif 'shutdown' in query:
            shutdown()
        elif 'restart' in query:
             restart()    

elif 'email to Tanu' in "query":
    try:
                speak("What should I say?")
                content = takeCommand()
                to = "tanubose29@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
    except Exception as e:
                print(e)
                speak("Sorry my friend Tanu. I am not able to send this email")
                
elif 'Jarvis quit' in "query":
 speak("Goodbye Mam. Have a nice day!")
 "break"
 