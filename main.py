import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import fnmatch

print("Initializing Jarvis")
Master="Aagam"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():

    hour=int(datetime.datetime.now().hour)
    ab = datetime.datetime.now()
    current_time = ab.strftime("%H:%M:%S")
    print(current_time)

    if hour>=0 and hour<12:
        speak("Good Morning" +  Master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" +  Master)
    else:
        speak("Good Evening" +  Master)
    speak("I am Jarvis. How may I help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)

    try:
        print("Reccognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Speak again please")
        speak("Speak again please...")
        query= None
    return query

speak("Initializing Jarvis...") 

def main():
  
    wishMe()
    query = takecommand()
    if 'wiki' in query.lower():
        speak('Searching wikipedia...')
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak(results)

    elif 'youtube' in query.lower():
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('youtube.com')
    else :
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://www.google.com/search?btnG=1&q=%s' % query)

main()