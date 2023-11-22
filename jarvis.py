import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    
    speak("I am siri mam. please tell me how may i help you")

def takecommand():
    #it takes microphone input fro the user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please....")
        return "None"
    return query


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('goyalshreya1012@gmail.com', 'exixjuepjdmrhztz')
    server.sendmail('goyalshreya1012@gmail.com', to , content)
    server.close()
     
if __name__=="__main__":
    # speak("shreya is a good student")
    wishme()
    while True:
        query=takecommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\PC\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"mam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to shreya' in query:
            try:
                print("what should I say")
                content = takecommand()
                to="shreyagoyal985@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry shreya.I am not able to send email")

