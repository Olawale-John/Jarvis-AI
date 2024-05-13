import random
import webbrowser
import wikipedia
import os
import linecache
import AppOpener

# .\pyinstaller --onedir --icon jarvis32.ico Jarvis.py
# .\pyinstaller --onefile --icon jarvis32.ico Jarvis.py

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
    if hour >= 0 and hour < 12:
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


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("See you later.")
            print("Goodbye (._.)")
            break

        elif "morning" in query:
            speak("Good morning sir, nice to chat with you again.")

        elif "words of encouragement" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "motivate" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "motivation" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "motivational quote" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "inspire" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "inspirational" in query:
            changeSpeedRate(180)
            encouragement()
            changeSpeedRate(200)

        elif "open browser" in query:
            speak("Are you sure?")
            query = takeCommand().lower()
            if "yes" in query:
                url = "https://google.com/search?q="
                speak("Opening web browser, please be patient, this might take a while...")
                print("Opening Browser...")
                webbrowser.get().open(url)
            elif "sure" in query:
                url = "https://google.com/search?q="
                speak("Opening web browser, please be patient, this might take a while...")
                print("Opening Browser...")
                webbrowser.get().open(url)
            else:
                reply = ["No offense, but be more precise next time please.", "No problem.", "Alright."]
                randomReply = random.randint(0, 2)
                botReply = reply[randomReply]
                speak(botReply)
                continue


        elif "open" in query:
            try:
                query = query.replace("open", "")
                speak(f"Opening {query}... This might take a while to load.")
                AppOpener.open(query)
            except Exception as e:
                speak("Failed to open.")
            continue

        elif "close" in query:
            command = query.replace("close", "")
            speak(f"Are you sure to close {command}?")
            query = takeCommand().lower()
            if "yes" in query:
                AppOpener.close(command)
            elif "sure" in query:
                AppOpener.close(command)
            else:
                speak("Alright!")
                continue

        elif "about me" in query:
            name = open("ownership.txt", "r")
            name = linecache.getline("ownership.txt", 1)
            name = name.replace("Name:  ", "")

            gender = open("ownership.txt", "r")
            gender = linecache.getline("ownership.txt", 3)
            gender = gender.replace("Gender:  ", "")

            dob = open("ownership.txt", "r")
            dob = linecache.getline("ownership.txt", 2)
            dob = dob.replace("Date of Birth:  ", "")

            speak(f"Your name is {name}. You are a {gender}, and your date of birth is {dob}")

        elif "afternoon" in query:
            speak("It is a beautiful and sunny one, I hope your skin is not too affected by the sun radiation.")

        elif "evening" in query:
            speak("My evening is a great one. Is yours?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("I am glad you are happy.")
            else:
                speak("I am here to make you feel better and answer all your questions.")

        elif "delete record" in  query:
            try:
                speak("Are you sure?")
                query = takeCommand().lower()
                if "yes" in query:
                    os.remove("data.txt")
                    speak("Deleted.")
                    print("Record Deleted...")
                elif "sure" in query:
                    os.remove("data.txt")
                    speak("Deleted.")
                    print("Record Deleted...")
                else:
                    speak("Alright.")
            except Exception as e:
                speak("No Record.")

        elif "delete friends" in  query:
            speak("Are you sure? This would delete all friends names.")
            try:
                query = takeCommand().lower()
                if "yes" in query:
                    os.remove("friends.txt")
                    speak("Deleted.")
                    print("Friends Names Deleted...")
                elif "sure" in query:
                    os.remove("friends.txt")
                    speak("Deleted.")
                    print("Friends Names Deleted...")
                else:
                    speak("Alright.")
            except Exception as e:
                speak("No previous record.")

        elif "delete all friends" in  query:
            speak("Are you sure? This would delete all friends names.")
            try:
                query = takeCommand().lower()
                if "yes" in query:
                    os.remove("friends.txt")
                    speak("Deleted.")
                    print("Friends Names Deleted...")
                elif "sure" in query:
                    os.remove("friends.txt")
                    speak("Deleted.")
                    print("Friends Names Deleted...")
                else:
                    speak("Alright.")
            except Exception as e:
                speak("No previous record.")

        elif "delete all record" in  query:
            speak("Are you sure? This would delete friends names also.")
            try:
                query = takeCommand().lower()
                if "yes" in query:
                    os.remove("data.txt")
                    os.remove("friends.txt")
                    speak("All Record Deleted.")
                    print("All Record Deleted...")
                elif "sure" in query:
                    os.remove("data.txt")
                    os.remove("friends.txt")
                    speak("All Record Deleted.")
                    print("All Record Deleted...")
                else:
                    speak("Alright.")
            except Exception as e:
                speak("No previous record.")

        elif "add friend name" in query:
            speak("What name is it?")
            data = takeCommand()
            note = open("friends.txt", "a")
            note.write(f"{data} \n")
            note.close()
            speak("I won't forget so easily.")
            continue

        elif "add friend's name" in query:
            speak("What name is it?")
            data = takeCommand()
            note = open("friends.txt", "a")
            note.write(f"{data} \n")
            note.close()
            speak("I won't forget so easily.")
            continue

        elif "add multiple friend's name" in query:
            speak("What name is it?")
            data = takeCommand()
            note = open("friends.txt", "a")
            data = data.replace(" ", "\n")
            note.write(f"{data} \n")
            note.close()
            speak("I won't forget so easily.")
            continue

        elif "thanks" in query:
            reply = ["No mention.", "That's what friends do.", "Anytime.", "Thank God.", "You are welcome"]
            randomReply = random.randint(0, 4)
            botReply = reply[randomReply]
            speak(botReply)

        elif "thank" in query:
            reply = ["No mention.", "Anytime.", "Thank God.", "You are welcome"]
            randomReply = random.randint(0, 3)
            botReply = reply[randomReply]
            speak(botReply)

        elif "nice" in query:
            speak("Such a honour.")

        elif "dear assistant" in query:
            reply = ["Yes boss.", "At your service boss.", "Yes sir.", "Boss.", "Sir."]
            randomReply = random.randint(0, 4)
            botReply = reply[randomReply]
            speak(botReply)

        elif "wikipedia" in query:
            speak("Searching...")
            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences = 2)
                changeSpeedRate(150)
                print(f"Searching: {query.capitalize()}")
                speak(result)
                changeSpeedRate(200)
            except Exception as e:
                speak("Can't find it on wikipedia. You can kindly rephrase the sentence.")

        elif "study on" in query:
            speak("Searching...")
            try:
                query = query.replace("study on", "")
                result = wikipedia.summary(query, sentences = 2)
                changeSpeedRate(150)
                print(f"Searching: {query.capitalize()}")
                speak(result)
                changeSpeedRate(200)
            except Exception as e:
                speak("Can't find it on wikipedia. You can kindly rephrase the sentence.")

        elif "multiverse" in query:
            speak("Accessing intelligent bot(multiverse) would automatically close this session. Do you agree?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Working on it... This might take a while...")
                import intelligent_bot
            else:
                speak("Alright.")
                continue

        elif "battery" in query:
            battery()

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot saved in pictures folder.")
            print("Screenshot saved...")

        elif "who are you" in query:
            speak("I am an artificial intelligence. I suppose you are human.")

        elif "logout computer" in query:
            speak("Are you sure to log computer out?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Logging Out...")
                print("Logging Out...")
                os.system("shutdown  /l")
            else:
                speak("Alright.")

        elif "what can you do" in query:
            speak("I can be your assistant. There would be an upgrade on me soon and I would be able to recognize face and do some other cool stuffs. But for the meantime, you can check my documentation in directory folder.")

        elif "your purpose" in query:
            try:
                name = open("ownership.txt", "r")
                name = linecache.getline("ownership.txt", 1)
                name = name.replace("Name:  ", "")
                speak(f"Please don't disturb me {name}.")
            except Exception as e:
                speak("Please don't disturb me.")

        elif "shut down computer" in query:
            speak("Are you sure to shut down computer?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Shutting Down...")
                print("Shutting Down...")
                os.system("shutdown /s /t 1")
            else:
                speak("Alright.")

        elif "restart computer" in query:
            speak("Are you sure to restart computer?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Restarting Computer...")
                print("Restarting Computer...")
                os.system("shutdown /r /t 1")
            else:
                speak("Alright.")


        elif "search" in query:
            speak("Searching... This would direct your search to browser and might take a while to load the browser app...")
            print("Redirecting Search...")
            query = query.replace("search", "")
            print(f"Searching: {query.capitalize()}")
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
            continue

        elif "make research" in query:
            speak("Researching... This would direct your search to browser and might take a while to load the browser app...")
            print("Redirecting Research...")
            print(f"Researching:{query.capitalize()}")
            url = "https://google.com/search?q=" + query
            webbrowser.get().open(url)
            continue

        elif "send mail" in query:
            try:
                speak("What is the message?")
                message = takeCommand()
                speak("Input receiver.")
                to = input("Send To: ")
                password = input("Confirm code: ")
                sendMail(to, message, password)
                speak("The mail was successfully sent.")
            except Exception as e:
                speak(f"{e}, unable to send mail.")

        elif "sleep" in query:
            speak("Going to sleep.")
            print("Sleeping...")
            wake = input("Wake me: ").lower()
            speak("Hello boss, I am awake and active now.")
            print("Awake...")
            continue

        elif "wake" in query:
            speak("I am already awake.")
            continue

        elif "best friend" in query:
            speak("You are my bestfriend. Would you like to share your friends name?")
            query = takeCommand().lower()
            if "yes" in query:
                speak("Alright. I would remember their names. Please say them.")
                data = takeCommand()
                note = open("friends.txt", "a")
                data = data.replace(" ", "\n")
                note.write(f"{data} \n")
                note.close()
                speak("I won't forget their names so easily.")
                continue
            elif "sure" in query:
                speak("Alright. I would remember their names. Please say them.")
                data = takeCommand()
                note = open("friends.txt", "a")
                data = data.replace(" ", "\n")
                note.write(f"{data} \n")
                note.close()
                speak("I won't forget their names so easily.")
                continue
            else:
                speak("Alright.")
                continue

        elif "your name" in query:
            speak("My name is Jarvis, one of the Artificial intelligence created by Olawale.")

        elif "invented" in query:
            speak("I was invented by Olawale Yahaya John.")

        elif "calculate" in query:
            try:
                print("Calculating...")
                query = query.replace("calculate", "")
                answer = eval(query)
                speak(f"{query} is equal {answer}.")
            except Exception as e:
                speak("Couldn't calculate it.")

        elif "my friend" in query:
            try:
                note = open("friends.txt", "r")
                changeSpeedRate(200)
                speak("I would mention the name of your friend that I know. It is " + note.read())
                changeSpeedRate(200)
            except Exception as e:
                speak("I do not have any record of your friends. Would you like to share their names?")
                query = takeCommand().lower()
                if "yes" in query:
                    speak("Alright. I would remember their names. Please say them.")
                    data = takeCommand()
                    note = open("friends.txt", "a")
                    data = data.replace(" ", "\n")
                    note.write(f"{data} \n")
                    note.close()
                    speak("I won't forget their names so easily.")
                    continue
                elif "sure" in query:
                    speak("Alright. I would remember their names. Please say them.")
                    data = takeCommand()
                    note = open("friends.txt", "a")
                    data = data.replace(" ", "\n")
                    note.write(f"{data} \n")
                    note.close()
                    speak("I won't forget their names so easily.")
                    continue
                else:
                    speak("Alright.")
                    continue

        elif "my friends" in query:
            try:
                note = open("friends.txt", "r")
                changeSpeedRate(200)
                speak("I would mention the names of your friends that I know. They are " + note.read())
                changeSpeedRate(200)
            except Exception as e:
                speak("I do not have any record of your friends. Would you like to share their names?")
                query = takeCommand().lower()
                if "yes" in query:
                    speak("Alright. I would remember their names. Please say them.")
                    data = takeCommand()
                    note = open("friends.txt", "a")
                    data = data.replace(" ", "\n")
                    note.write(f"{data} \n")
                    note.close()
                    speak("I won't forget their names so easily.")
                    continue
                elif "sure" in query:
                    speak("Alright. I would remember their names. Please say them.")
                    data = takeCommand()
                    note = open("friends.txt", "a")
                    data = data.replace(" ", "\n")
                    note.write(f"{data} \n")
                    note.close()
                    speak("I won't forget their names so easily.")
                    continue
                else:
                    speak("Alright.")
                    continue

        elif "save friend name" in query:
            speak("What name is it?")
            data = takeCommand()
            note = open("friends.txt", "a")
            note.write(f"{data} \n")
            note.close()
            speak("I won't forget so easily.")
            continue

        elif "change to female voice" in query:
            changeVoice("female")
            speak("Voice Changed...")
            print("Voice Changed...")

        elif "change to male voice" in query:
            changeVoice("male")
            speak("Voice Changed...")
            print("Voice Changed...")

        elif "how are you" in query:
            reply = ["Better than ever. Only God controls this.", "Copacetic. You should too, align with God.", "In perfect shape.", "Happy to commune with you. Please commune with God also.", "Well, my connection is all fine, I hope you are in connection with God."]
            randomReply = random.randint(0, 4)
            botReply = reply[randomReply]
            speak(botReply)

        elif "play song" in query:
            try:
                songs_dir = r"C:\Users\user\Music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
                speak("Playing...")
                print("Playing Song...")
            except Exception as e:
                speak("No song in your music folder directory")

        elif "sing" in query:
            try:
                songs_dir = r"C:\Users\user\Music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
                speak("Playing...")
                print("Playing Song...")
            except Exception as e:
                speak("No song in your music folder directory")

        elif "play music" in query:
            try:
                songs_dir = r"C:\Users\user\Music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))
                speak("Playing...")
                print("Playing Music...")
            except Exception as e:
                speak("No song in your music folder directory")

        elif "note" in query:
            speak("What should I take note of?")
            data = takeCommand().capitalize()
            speak("I would remember for as long as you want me to.")
            note = open("data.txt", "a")
            note.write(f"{data} \n")
            note.close()

        elif "record" in query:
            speak("What should I keep record of?")
            data = takeCommand().capitalize()
            speak("I would remember for as long as you want me to.")
            note = open("data.txt", "a")
            note.write(f"{data} \n")
            note.close()

        elif "what do you remember" in query:
            try:
                note = open("data.txt", "r")
                changeSpeedRate(220)
                speak("You told me to take note of " + note.read())
                changeSpeedRate(200)
            except Exception as e:
                speak("I do not remember anything.")

        elif "joke" in query:
            jokes()

        elif "embarrassed" in query:
            speak("Would you love to share what embarrassed you?")
            query = takeCommand().lower()
            if "yes" or "sure" in query:
                speak("I am all ears...")
                takeCommand()
                speak("Oh wow! Thanks for confiding in me, but regardless of what so ever comes your way, you are a work in progress. Move on with life, as what you have faced is a stepping stone and not an obstacle.")
            else:
                speak("Alright, just make sure you are okay. I was designed to make you feel better.")

        elif "what is" in query:
            try:
                query = query.replace("what is", "")
                result = wikipedia.summary(query, sentences = 1)
                changeSpeedRate(150)
                print(f"Wikipedia: {query.capitalize()}")
                speak(result)
                changeSpeedRate(200)
            except Exception as e:
                pass


        else:
            reply = ["Kindly repeat.", "Try again.", "Speak again.", "I do not have noise cancellation.",
                     "Don't forget to study your bible.", "Do you want to know what I remember?"]
            randomReply = random.randint(0, 5)
            botReply = reply[randomReply]
            speak(botReply)