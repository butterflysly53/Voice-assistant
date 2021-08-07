import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id )
newVoiceRate=200
engine.setProperty('rate',newVoiceRate)

#First greeting from Ai assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is Friday,Your AI assistant")

#For saying Current Time
def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)

#For saying Current Date
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

#Greetings of friday
def wishme():
    speak("welcome back")
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Friday at your service  How can I help You")

#wishme()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language= 'en=IN')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please..")
        return "None"
    return query

#alternative takeCommand function 
'''def takeCommand():

    r = sr.Recognizer()



    with sr.Microphone() as source:

        print("listening...")

        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 1

        audio = r.listen(source)

        try:

            print("Recognising...")
            print (r.recognize_google(audio,language = 'en-in'))

        except Exception as e:

            print("Error :  " + str(e))

            speak("Repeat the speech again")

            return "None"

        with open("recorded.wav", "wb") as f:

            f.write(audio.get_wav_data())

takeCommand()'''
#for sending email
def send_email(to, content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("your@gmail.com", "password") #enter your emailid and password
    server.sendmail("your@gmail.com", to, content)
    server.quit()

#for taking screenshot
def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\Image\ss.png") #give the path where screenshots will be stored

#for knowing cpu and battery usuage
def cpu():
    usage= str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

#for telling jokes 
def jokes():
    speak(pyjokes.get_joke())

#main function
if __name__=="__main__":

    wishme()
    while True:
    #this loop will stop executing when user will say "Offline"
        query=takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)

        elif "send email" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to= "receiver@gmail.com" #give receiver's email-id
                sendmail(to, content)
                speak(content)
                speak("Email has been sent suceesfully!")
            except Exception as e:
                speak(e)
                speak("Email is not sent!")

        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "logout" in query:
            os.system("shutdown -l")
        
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "remember that" in query:
            speak("What should I remember?")
            data=takeCommand()
            speak("You told me to remeber that" + data)
            remember=open("data.text","w")
            remember.write(data)
            remember.close()
       
        elif "do you know anything" in query:
            remember=open("data.text", "r")
            speak("you said me to remember that" + remember.read())
       
        elif "screenshot" in query:
            screenshot()
            speak("screenshot taken!")
       
        elif "cpu" in query:
            cpu()
        
        elif "jokes" in query:
            jokes()

        elif "offline" in query:
            quit()
        
        

    





        
            
        











