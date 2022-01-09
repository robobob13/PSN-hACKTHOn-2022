import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import datetime
import smtplib
from pygame import mixer
import os
import turtle as t
import keyboard


BotText = "Speak"
srr = sr.Recognizer()
current_time = datetime.datetime.now()
engine=pyttsx3.init()
usertext = ""



def SpeakText(command): #Speaks the text you put in command
    engine.say(command)
    engine.runAndWait()
def GoogleSearchResults(SearchQuery):
  from googlesearch import search
  for j in search(SearchQuery, tld="co.in"and"com", num=5, stop=5, pause=1):
    print(j)
    webbrowser.open(j)
    time.sleep(0.2)
    
def CreateZoomMeeting(ZoomMeetingTitle, MeetingDuration, ZoomMeetingAgenda, StartTime):
    import jwt
    import requests
    import json
    from time import time
    '''
    response = requests.post("https://zoom.us/oauth/authorize", )
    print(response.status_code)
    print(response.json())
    '''

    API_KEY = 'W_vbJQwpSA-ixnTmASm1bw'
    API_SEC = 'yWVY5JWux4GLGXurhptYfrL3LoPpPGljIXRY'

    def generateToken():
        token = jwt.encode(

            {'iss': API_KEY, 'exp': time() + 5000},

            API_SEC,

            algorithm='HS256'
        )
        return token

    meetingdetails = {"topic": ZoomMeetingTitle,
                      "type": 2,
                      "start_time": StartTime,
                      "duration": MeetingDuration,
                      "timezone": 'Asia/India',
                      "agenda": ZoomMeetingAgenda,

                      "recurrence": {"type": 1,
                                     "repeat_interval": 1
                                     },
                      "settings": {"host_video": "true",
                                   "participant_video": "true",
                                   "join_before_host": "true",
                                   "mute_upon_entry": "False",
                                   "watermark": "true",
                                   "audio": "voip",
                                   "auto_recording": "cloud"
                                   }
                      }

    def createMeeting():
        headers = {'authorization': 'Bearer %s' % generateToken(),
                   'content-type': 'application/json'}
        r = requests.post(
            f'https://api.zoom.us/v2/users/me/meetings',
            headers=headers, data=json.dumps(meetingdetails))

        print("\n creating zoom meeting ... \n")
        y = json.loads(r.text)
        join_URL = y["join_url"]
        meetingPassword = y["password"]

        print(
            f'\n Here is your zoom meeting link {join_URL} and your \
            password: "{meetingPassword}"\n')
        webbrowser.open(join_URL)

    return createMeeting()



def speak(): #It takes ur mic input
    try:
        with sr.Microphone() as source2:
            srr.adjust_for_ambient_noise(source2,duration=0.7)
            BotText = "Speak"
            print(BotText)
            SpeakText(BotText)
            audio2=srr.listen(source2)
            MyText = ""
            try:
                MyText=srr.recognize_google(audio2)
            except sr.UnknownValueError as u:
                pass
            MyText=MyText.lower()
            usertext = MyText
            print(usertext)
            print("Stop")
            return MyText
    except sr.RequestError as s:
        print("an error occur")

voices = engine.getProperty('voices')
print("Welcome To ViaAI!")
SpeakText("Welcome To via AI")
time.sleep(0.3)
print("This is an AI made for our 2022 PSN Hackathon Project")
SpeakText("This is an AI made for our 2022 PSN Hackathon Project")
time.sleep(0.3)
print("Made By: Aaryamaan Saini, Agastya Gupta, Saksham Gupta")
SpeakText("Made By Aaryamaan Saini, Agastya Gupta, Saksham Gupta")
time.sleep(0.3)
usertext=""
BotText=""

from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import time

RecQuestionState=False
MenuState=False


def RecordButtonPressed(truth):
    if truth == True:
        
        RecQuestionState=True
        return


class GiveCommands:
    pass


def ListenToUser():
    Input = speak()

    
    spec = "Speak"

# To add the command put under this while true loop, put an elif saying (elif "command" in Input:)
    cless = {'8:30':'Form Time',
     '9:00':"Lesson 1",
     "10:00":"Lesson 2",
     "11:00":"Lesson 3",
     "12:00":"Lesson 4",
     "13:35":"Lesson 5",
     "14:25":"Lesson 6",
     "19:37":"Test"}
     
    timone = str(current_time.hour)+":"+str(current_time.minute)
    
    for timmy, cLass in cless.items():
        if timone == timmy:
            amogus = "Time for, "+cLass
            print(amogus)
            SpeakText(amogus)
    if "school" in Input: #If you say school then this happens
        print("Opening School Related Tabs")
        SpeakText("Opening school related tabs")
        webbrowser.open('https://classroom.google.com/u/0/h')
        time.sleep(0.5)
        webbrowser.open('https://teams.microsoft.com/')
        time.sleep(0.5)
        webbrowser.open('https://docs.google.com/document/u/0/?tgif=d')
        time.sleep(0.5)
        webbrowser.open('https://outlook.office365.com/owa/?realm=pathways.in&exsvurl=1&ll-cc=1033&modurl=0')
        time.sleep(0.5)
        webbrowser.open('https://psn.wizemen.net/')
        time.sleep(0.5)
        webbrowser.open('https://drive.google.com/drive/u/0/')
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)
    elif "time" in Input: #Says the time
        pm = False
        am = ""
        currtime = 0
        print("Year:", current_time.year)
        time.sleep(0.2)
        print("Month:", current_time.month)
        time.sleep(0.2)
        print("Day:", current_time.day)
        date = "The Day is:",current_time.day,"of the month",current_time.month,"and is the year",current_time.year
        SpeakText(date)
        time.sleep(1)
        if current_time.hour > 12:
            currtime = current_time.hour - 12
            pm = True
        else:
            currtime = current_time.hour
        if pm == True:
            am = "pm"
        else:
            am = "am"
        currtime = str(currtime)
        timone = currtime, current_time.minute,am,"and",current_time.second,"seconds"
        print(currtime+":"+str(current_time.minute)+":"+str(current_time.second))
        SpeakText(timone)
        
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)
    elif 'youtube' in Input:
        print("Opening Youtube...")
        SpeakText("opening youtube")
        webbrowser.open("https://www.youtube.com")
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)

    elif 'google' in Input:
        print("What do you want to search?")
        SpeakText("what do you want to search")
        query = speak()
        GoogleSearchResults(query)

        time.sleep(15)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)

    elif 'gmail' in Input:
        print("Opening Gmail...")
        SpeakText("opening gmail")
        webbrowser.open("https://www.gmail.com")
        
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)
    elif 'voice' in Input:
        print("You can change my voice to male or female")
        SpeakText("You can change my voice to male or female")
        time.sleep(0.2)
        print("Say female to change my voice to female, or say male to change my voice to male")
        SpeakText("say female to change my voice to female, or say male to change my voice to male")
        gender = speak()
        if 'mail' in gender:
            engine.setProperty('voice', voices[len(voices)-3].id)
        elif 'female' in gender:
            engine.setProperty('voice', voices[len(voices)-2].id)
        else:
            print("Invalid input")
            SpeakText("invalid input")
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)
    elif 'zoom' in Input:
        print("What is the meeting name?")
        SpeakText("What is the meeting name")
        name = speak()
        time.sleep(0.2)
        duration = 40
        time.sleep(0.2)
        print("What is the meeting agenda?")
        SpeakText("What is the meeting agenda")
        agenda = speak()
        time.sleep(0.2)
        finaldate = str(current_time.year)+"-"+str(current_time.month)+"-"+str(current_time.day)+"T"+str(current_time.hour)+": "+str(current_time.minute)+": "+str(current_time.second)
        print(CreateZoomMeeting(name,duration,agenda,finaldate))
        SpeakText("zoom meeting made")
        time.sleep(5)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)
        
    elif 'stop' in Input:
        print("Good Bye!")
        SpeakText("good bye")
        time.sleep(0.2)
    elif 'pause' in Input:
        print("Press Space Bar to continue")
        SpeakText("Press Space Bar To Continue")
        while True:
            cless = {'8:30':'Form Time',
                     '9:00':"Lesson 1",
                     "10:00":"Lesson 2",
                     "11:00":"Lesson 3",
                     "12:00":"Lesson 4",
                     "13:35":"Lesson 5",
                     "14:25":"Lesson 6",
                     "19:37":"Test"}
     
            timone = str(current_time.hour)+":"+str(current_time.minute)
    
            for timmy, cLass in cless.items():
                if timone == timmy:
                    amogus = "Time for, "+cLass
                    print(amogus)
                    SpeakText(amogus)
            if keyboard.is_pressed("space"):
                break
        time.sleep(2)
        print("Restarting Program")
        SpeakText("Restarting Program")
        time.sleep(0.3)

    else:
        print("I did not understand, please try again")
        SpeakText("I did not understand, please try again")
        time.sleep(0.5)

            





root = tk.Tk()
root.geometry("1200x781") # Size of background board
canvas = tk.Canvas(root, width=1200, height=781)
canvas.place(x=0,y=0)
background_image = tk.PhotoImage(file="how-to-create-cool-website-backgrounds-the-ultimate-guide (1).png")
canvas.create_image((0,0), anchor="nw", image=background_image)


# Create button
im = Image.open("noun-mic-2222591.png").resize((350,350))
imTk =  ImageTk.PhotoImage(im)
im1 = Image.open("noun-mic-2222593.png").resize((350,350))
imTk1 =  ImageTk.PhotoImage(im1)


Recording = canvas.create_image((400,50), anchor="nw", image=imTk)
canvas.tag_bind(Recording, '<Button-1>', lambda x: ListenToUser())


SettingsButton=Button(root, text="Settings", command=GiveCommands)
AboutUs=Button(root, text="About Us", command=GiveCommands)
Commands=Button(root, text="Commands", command=GiveCommands)
Commands.place(x=20,y=20,)
AboutUs.place(x=20,y=50,)
SettingsButton.place(x=20,y=80,)
Rectangle=canvas.create_rectangle(20,60,20,60, fill="white")

UserTextShow = Text(root, height=15, fg="white", bg="purple", width=70)
UserTextShow.place(x=600, y=400)
root.wm_attributes("-alpha", 0.994)
UserTextShow.insert(tk.END, usertext)
UserTextShow.insert(tk.END, " ")

BotTextShow = Text(root, height=15, fg="white", bg="purple", width=70)
BotTextShow.place(x=25, y=400)
root.wm_attributes("-alpha", 0.994)
BotTextShow.insert(tk.END, BotText)
BotTextShow.insert(tk.END, " ")


tk.mainloop()




