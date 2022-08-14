import time
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine=pyttsx3.init()

music_path=""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("Current time is ")
    speak(Time)
def Date():
    x=datetime.datetime.now()
    year=int(x.year)
    month=int(x.month)
    date=int(x.day)
    speak("Current Date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Hello Sir! This is JARVIS")
    Time()
    Date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("How can I help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        #r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query= r.recognize_google(audio,language='en-pk')
        print(query)
    except Exception as e:
        print(e)
        speak("Say That Again Please.....")
        return "None"
    return query

def Search_Wiki(query):
    speak("Searching Wikipedia....")
    result=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    print(result)
    speak(result)

def saythistothis(query):
    try:
        strr=''.join(query.split('say')[1].split('to'))
        speak(strr)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        check_query=query.lower()

        if check_query=="hello jarvis":
            wishme()
            speak("Hello Sir!")
        elif 'wikipedia' in check_query:
            query=query.replace('Wikipedia','')
            Search_Wiki(query)
        elif 'open google' in check_query:
            webbrowser.open('www.google.com')
        elif 'play music' in check_query:
            songs=os.listdir(music_path)
            speak('Playing Music....')
            for i in songs:
                song=os.path.join(music_path,i)
                os.startfile(song)
                time.sleep(len(i))
        elif 'google' in check_query or 'search' in check_query:
            a=query.split()
            if a[0]=="search":
                search_q=' '.join(a[1:-2])
                search='https://www.google.com/search?q='+search_q
                webbrowser.open(search)
        elif 'news' in check_query:
            news = webbrowser.open_new_tab("https://www.thenews.com.pk/")
            speak('Here are some headlines from the The News ,Happy reading')
            time.sleep(6)
        elif 'say' in check_query:
            saythistothis(query)
        elif check_query=="stop jarvis" or check_query=="jarvis stop":
            speak(" Good By Sir!")
            break
        else:
            speak('Speak again Sir!')