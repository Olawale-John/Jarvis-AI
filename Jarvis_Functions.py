import psutil
import pyttsx3
import pyjokes
import datetime
import smtplib
import random
import linecache
import pyautogui
import speech_recognition as sr

engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def changeVoice(gender):
    voices = engine.getProperty("voices")
    if gender.lower() == "male":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

def changeSpeedRate(speed_rate):
    engine.setProperty("rate", speed_rate)

def time():
    time = datetime.datetime.now().strftime("%I:%M")
    speak(f"The time is {time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"Today's date is {day} {month} {year}.")

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        greetings = "Good morning."
    elif hour >= 12 and hour < 17:
        greetings = "Good afternoon."
    else:
        greetings = "Good evening."

    try:
        name = open("ownership.txt", "r")
        name = linecache.getline("ownership.txt", 1)
        name = name.replace("Name:  ", "")

        gender = open("ownership.txt", "r")
        gender = linecache.getline("ownership.txt", 3)
        gender = gender.replace("Gender:  ", "")

        if gender == "Male" + "\n":
            speak(f"{greetings} mister {name}. How can I help you?")
        elif gender == "male" + "\n":
            speak(f"{greetings} mister {name}. How can I help you?")
        elif gender == "Female" + "\n":
            speak(f"{greetings} miss {name}. How can I help you?")
        elif gender == "female" + "\n":
            speak(f"{greetings} miss {name}. How can I help you?")
        else:
            speak(f"Good Morning {name}. How can I help you?")

    except Exception as e:
        print("Hey user, there is no prove for ownership. I would like to know your name and some other details.")
        name = input("Name: ")
        dob = input("Date of Birth: ")
        gender = input("Gender: ").lower()
        with open("ownership.txt", "a") as t:
            t.write("Name:" + "  " + name.capitalize() + "\n")
            t.write("Date of Birth:" + "  " + dob.capitalize() + "\n")
            t.write("Gender:" + "  " + gender.capitalize() + "\n")
            t.close()
        print("Saved !")

        name = open("ownership.txt", "r")
        name = linecache.getline("ownership.txt", 1)
        name = name.replace("Name:  ", "")

        gender = open("ownership.txt", "r")
        gender = linecache.getline("ownership.txt", 3)
        gender = gender.replace("Gender:  ", "")

        if gender == "Male" + "\n":
            speak(f"{greetings} mister {name}. How can I help you?")
        elif gender == "male" + "\n":
            speak(f"{greetings} mister {name}. How can I help you?")
        elif gender == "Female" + "\n":
            speak(f"{greetings} miss {name}. How can I help you?")
        elif gender == "female" + "\n":
            speak(f"{greetings} miss {name}. How can I help you?")
        else:
            speak(f"Good Morning {name}. How can I help you?")

def changeName():
    speak("What name are you changing to?")
    try:
        Newname = input("New name: ").capitalize()
        name = open("ownership.txt", "r")
        name = linecache.getline("ownership.txt", 1)
        name = name.replace(name, f"Name:  {Newname}")
        print("Name Changed...")
        speak(f"Successful, your new name is {name}")
    except Exception as e:
        print("Unsuccessful...")
        speak("Unsuccessful.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        voice_data = r.recognize_google(audio)
        # print(voice_data)
    except Exception as e:
        print("Error Message...")
        # speak("Ensure you have access to the internet connection. Would you prefer to type?")
        # type_option = input("Type y for yes and n for no: ").lower()
        # if type_option == "n":
        #     speak("See you later.")
        #     quit()
        # else:
        #     speak("Alright! All hands on deck boss. I would love to see you express your emotions in written words.")
        #     pass
        return "None."
    return voice_data

def sendMail(to, message, password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("olawalejohn081@gmail.com", password)
    server.sendmail("olawalejohn081@gmail.com", to, message)
    server.close()

def screenshot():
    try:
        img = pyautogui.screenshot()
        img.save("C:\\Users\\user\\Pictures\\Jarvis_Screenshot.png")
    except Exception as e:
        speak("Couldn't take screenshot.")

def battery():
    cpu_usage = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery()
    speak("I have" + str(battery_percent.percent) + " percentage battery.")

def jokes():
    changeSpeedRate(170)
    speak(pyjokes.get_joke())
    changeSpeedRate(200)

def aboutJarvis(query):
    # if "what is your name" in query:
    pass

def ownership():
    pass

def encouragement():
    reply = ["Affliction will not rise the second time. The Holy Bible said that in Nahum 1 verse 9",
             "Never stay back on the ground, bounce back and tremble the earth with your prescence.",
             "If you feel like quiting, look around you and see the chaos others are facing. It is not just about you",
             "Remember that the troubles of this world are nothing compared to the latter glory.",
             "Miracle no dey tire Jesus. He is ready to bless you too.",
             "Light awaits you at the end of the tunnel, keep digging. Don't be deceived by cruise.",
             "It's not the size of the dog in the fight, but the size of the fight in the dog.",
             "Nothing lasts forever, not even your troubles",
             "Encouragements don't last, your passion does. Make decisions now!",
             "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle",
             "Take chances, make mistakes. That's how you grow. Pain nourishes your courage. You have to fail inorder to practice being brave.",
             "If you don't go after what you want, you will never have it. If you don't ask, the answer is always no. If you don't step forward, you are always in the same place.",
             "The only place you find success before work is in the dictionary.",
             "You are going to fail your way to success, you have nothing to be ashamed of so keep your head up. I is much easier to come up with excuses of why you can't do it. If you do what is easy, your life will be hard.",
             "A life spent making mistakes is not only more honorable, but more useful than a life spent doing nothing.",
             "Nobody can make you feel inferior without your consent.",
             "I quit being afraid when my first venture failed and the sky didn't fall down.",
             "Hope never abandons you, you abandon it.",
             "The only thing keeping you from getting what you want is the story you keep telling yourself about why you don't have it. People who are willing to die to succeed will tend to succeed.",
             "Don't sit down and wait for opportunities to come, get up and make them."
             "Jesus said, 'in the world you will have tribulation. But take heart; I have overcome the world.' John 16 verse 33.",
             "All things work together for the good of those who love God. Romans 8 verse 28.",
             "Be strong and of good courage. Do not be frightenend, and do not be dismayed, for the Lord your God is with you whereever you go. Joshua 1 verse 9"
             "Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge Him, and He will make straight your path. Proverbs 3 verse 5-6",
             "crawling is acceptable, walking is acceptable, but stagnancy isn't.",
             "Be there for others, but never leave yourself behind."]
    randomReply = random.randint(0, 26)
    botReply = reply[randomReply]
    speak(botReply)
