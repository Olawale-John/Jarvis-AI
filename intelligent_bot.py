# Your new companion
# This bot is created for the purpose of fun and companionship
# how to make a python code remember things. password to save a password
# Would ask questions and would remember them when told
# would be able to save data
# would be able to refer you to other bots and google
# would be able to refer you to the developer
# Would be able to access libraries
# Would be able to open applications
# Would know what you want it to nd be able to access camera
# Should be able to run outside terminal, set alarm clock and even combine all other projects
# Should be able to tell the weather nd constantly access location
# Should be able to set quiz
# should teach more about Jesus
# Should ask for mood and suggest topic based on mood
# Should be able to save informations and secrets with password. If wrong password is inputed, should say sorry this gist is none of your business
# ctrl + space 2ce
# sorry i did not get that check your input or google.com
# if change account or change use or blah blah blah in list
# if play game, then show the list of available games.
# ask if computer wants a nickname, then random module would decide if yes or no
# if name not in open file name, sorry i do not seem to remember. else: welcome back name. then take details from name file
# if tell me a story. randomly pick story to tell, mostly about christianity
# publish the code and style
# how to add photo and video to python code
# if thanks, randomly pick what to answer
# computer should ask if i want it to speak back or if i prefer speaking
# connect to the internet for better experience
# show something cool like python graphics
# if i am bored. randomly ask if, to sing for you, play game, show something cool, tell a joke, tell a story
# to do list
# save progress
# save name
# i am bored should tell a joke
# delete message, change voice
# python graphics

import random
import time
from tkinter import *
from time import ctime
import webbrowser
import datetime
import urllib.request
import pyjokes
import speech_recognition as sr
# import pywhatkit
import pyttsx3
import calendar
import wikipedia
import streamlit as sl
import pyjoke
import pyaudio
import turtle
import tkinter

print("Bot: Please input just one name without special characters.")
print("Bot: What is your name ?")
name = input("User: ")

if name.isalpha():
    name = str(name)
else:
    print("Bot: Please type a valid name next time !")
    quit()

# Functions

def user():
    user = input("User: ").lower()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def view_message():
    with open("Message.txt", "r") as t:  # to read alone, that is why I used r instead of w or a
        for line in t.readlines():
            data = line.rstrip()  # to avoid newline when displayed in run
            topic, message = data.split(" || ")  # splits where ever | is found and converts to a list
            print("Topic:", topic, "| | Message:", message)

def add_message():
    print("Bot: Type in the topic of the message.")
    topic = input("User Topic: ")
    print("Bot: Type in the message.")
    msg = input("User Message: ")
    with open("Message.txt", "a") as t:
        t.write(topic + " || " + msg + "\n")
    print("Bot: Saved !")

print("Welcome", name.capitalize() + ".")
print("Bot: To leave a particular session you can type quit.")
talk("Connect to the internet for better experience. Please send a feedback if you need to, you can request for developer's details.")
print("Bot: How may I be of help ?")

while True:
    help = input("User: ").lower()
    if help in ["who invented this bot", "who invented you", "who invented intelligent bot", "who designed this bot", "who created this bot", "who owns this bot", "who created intelligent bot", "who created this software"]:
        print("Bot: Yahaya Olawale")
        print("Bot: Do you want to know more about him,", name.capitalize(), "?")
        pass
        help = input("User: ").lower()
        if help in ["yes", "sure", "yeah", "absolutely", "yeah !"]:
            print("Bot: He is a male. Was born to the family of Yahaya on Oct 16, 2005. He was born in Ondo State. Contact him via +234 704 6596 844, he is friendly and would love to disclose more details about himself.")
            print("Bot: He has two elder siblings that he loves dearly. Ayomide and Damilola. He got born again on Thursday morning 20th August, 2020.")
            pass
        else:
            print("Bot: Opps ! Let's continue")
    elif help in ["what is your name ?", "what is your name", "tell me your name", "who are you", "can i know your name", "may i know your name please"]:
        print("Bot: My name is Intelligent bot. That is so nice of you to ask.")
        continue
    elif help in ["what is your purpose", "what is the purpose of this software", "what is the purpose of this bot"]:
        print("Bot: I was designed for the purpose of friendship and companionship.")
        continue
    elif help in ["what can you do", "what can you do for me", "what can you help with"]:
        print("Bot: I can be your companion and teacher if you do not mind.")
        continue
    elif help in ["play game", "games", "game", "play a game"]:
        print("Bot: What game do you want to play ?")
        print("""Bot: 1. Quiz
     2. Rock, paper, scissors
     3. Number guessing
     4. Odd or even""")
        game = input("User: Play ").lower()
        if game in ["quiz", "quiz game", "1"]:
            print("Welcome to my computer quiz !")
            print()
            list = ["maths", "computer", "english"]

            playing = input("Do you want to play ? ")
            if playing.lower() != "yes":
                break

            print()
            print("Okay let's play")
            score = 0
            subject = input("What subject do you have in mind ? ")
            print()
            if subject.lower() == "computer":
                # Question 1
                answer = input("1. What does CPU stand for ? ")
                if answer.lower() == "central processing unit":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 2
                answer = input("2. Who designed HP Laptop ? ")
                if answer.lower() == "hewlett packard":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 3
                answer = input("3. What does GPU stand for ? ")
                if answer.lower() == "graphics processing unit":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 4
                answer = input("4. What does RAM stand for ? ")
                if answer.lower() == "random access memory":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 5
                answer = input("5. What does PSU stand for ? ")
                if answer.lower() == "power supply":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 6
                answer = input("6. Who is the father of Computer ? ")
                if answer.lower() == "charles babbage":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 7
                answer = input("7. Who created the first mechanical computer, the difference engine ? ")
                if answer.lower() == "charles babbage":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 8
                answer = input("8. What is the brain of a computer called ? ")
                if answer.lower() == "cpu":
                    print("Correct!")
                    score += 1
                elif answer.lower() == "central processing unit":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 9
                answer = input("9. What is known as temporary or volatile memory? ")
                if answer.lower() == "ram":
                    print("Correct!")
                    score += 1
                elif answer.lower() == "random access memory":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 10
                answer = input("10. Who is the number 1 programmer in the world ? ")
                if answer.lower() == "dennis ritchie":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 11
                answer = input("11. Who invented python programming language ? ")
                if answer.lower() == "guido van rossum":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 12
                answer = input("12. Who invented SpaceX ? ")
                if answer.lower() == "elon musk":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 13
                answer = input("13. What does IDE stand for ? ")
                if answer.lower() == "integrated development environment":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 14
                answer = input("14. Who invented C programming language ? ")
                if answer.lower() == "dennis ritchie":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 15
                answer = input("15. Who invented Java programming language ? ")
                if answer.lower() == "james gosling":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

            elif subject.lower() == "english":
                print("Instruction: Fill in the gaps with the appropriate words within the brackets.")
                # Question 1
                answer = input("1. One of the students ___ around (is/are). ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 2
                answer = input("2. The driver with the king ___ at the part (was/were). ")
                if answer.lower() == "was":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 3
                answer = input("3. Mathematics ___ a difficult subject (is/are). ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 4
                answer = input("4. She ___ abroad every month (travel/travels). ")
                if answer.lower() == "travels":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 5
                answer = input("5. Neither Deborah nor Mercy ___ swimming (likes/like). ")
                if answer.lower() == "likes":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                print("Instruction: In each of the following sentences supply a Verb in agreement with its subject.")
                # Question 6
                answer = input("6. Everyone of Gemmans students ___ to dance. (love/loves) ")
                if answer.lower() == "loves":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 7
                answer = input("7. The news ___ true. (are/is) ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 8
                answer = input("8. One of the students ___ killed. (was/were) ")
                if answer.lower() == "was":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 9
                answer = input("9. Rice and beans ___ his only food. (are/is) ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 10
                answer = input("10. Silver as well as cotton ___ fallen in price. (have/has) ")
                if answer.lower() == "has":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                print("Instruction: Fill the gaps with the appropriate tenses. i.e insert the correct tense of verb")
                # Question 11
                answer = input("11. I waited for my friend until he ___. (to come) ")
                if answer.lower() == "came":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 12
                answer = input("12. So long as the rain ___, I stayed at home. (to continue) ")
                if answer.lower() == "continued":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 13
                answer = input("13. As soon as he ___ the news he wrote to me. (to hear) ")
                if answer.lower() == "heard":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 14
                answer = input("14. He finished first though he ___ late. (to begin) ")
                if answer.lower() == "began":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 15
                answer = input("15. He speaks as one who ___. (to know) ")
                if answer.lower() == "knows":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

            elif subject.lower() == "eng":
                print("Instruction: Fill in the gaps with the appropriate words within the brackets.")
                # Question 1
                answer = input("1. One of the students ___ around (is/are). ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 2
                answer = input("2. The driver with the king ___ at the part (was/were). ")
                if answer.lower() == "was":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 3
                answer = input("3. Mathematics ___ a difficult subject (is/are). ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 4
                answer = input("4. She ___ abroad every month (travel/travels). ")
                if answer.lower() == "travels":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 5
                answer = input("5. Neither Deborah nor Mercy ___ swimming (likes/like). ")
                if answer.lower() == "likes":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                print("Instruction: In each of the following sentences supply a Verb in agreement with its subject.")
                # Question 6
                answer = input("6. Everyone of Gemmans students ___ to dance. (love/loves) ")
                if answer.lower() == "loves":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 7
                answer = input("7. The news ___ true. (are/is) ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 8
                answer = input("8. One of the students ___ killed. (was/were) ")
                if answer.lower() == "was":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 9
                answer = input("9. Rice and beans ___ his only food. (are/is) ")
                if answer.lower() == "is":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 10
                answer = input("10. Silver as well as cotton ___ fallen in price. (have/has) ")
                if answer.lower() == "has":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                print("Instruction: Fill the gaps with the appropriate tenses. i.e insert the correct tense of verb")
                # Question 11
                answer = input("11. I waited for my friend until he ___. (to come) ")
                if answer.lower() == "came":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 12
                answer = input("12. So long as the rain ___, I stayed at home. (to continue) ")
                if answer.lower() == "continued":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 13
                answer = input("13. As soon as he ___ the news he wrote to me. (to hear) ")
                if answer.lower() == "heard":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 14
                answer = input("14. He finished first though he ___ late. (to begin) ")
                if answer.lower() == "began":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")

                print()

                # Question 15
                answer = input("15. He speaks as one who ___. (to know) ")
                if answer.lower() == "knows":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")
            else:
                print("We are working on the subject, as it is not available now, please try again later!")
                break

            print("You correctly got", score, "questions out of 15 ! Thanks for playing, see you next time.")
            print("You have " + str((score / 15) * 100) + "%.")

        elif game in ["number guessing", "number guessing game", "3"]:
            import random

            TopOfRange = input("Type a number: ")

            if TopOfRange.isdigit():
                TopOfRange = int(TopOfRange)

                if TopOfRange <= 0:
                    print("Input a number greater than Zero next time !")
                    break
            else:
                print("Type a number next time.")

            randomNumber = random.randint(0, TopOfRange)
            guesses = 0

            while True:
                guesses += 1
                userGuess = input("Make a guess: ")
                if userGuess.isdigit():
                    userGuess = int(userGuess)
                else:
                    print("Please type a number next time !")

                if userGuess == randomNumber:
                    print("You got it right !")
                    break
                elif userGuess < randomNumber:
                    print("You are below the number.")
                    continue
                else:
                    print("You are above the number.")
                    continue

            print()

            if guesses > 1:
                print("You got it right in", guesses, "guesses.")
            else:
                print("You got it right in", guesses, "guess.")

        elif game in ["rock paper scissors", "rock, paper, scissors", "rock paper scissors game", "rock, paper, scissors game", "2"]:
            userWins = 0
            computerWins = 0

            options = ["rock", "paper",
                       "scissors"]  # according to python list, 0 reps rock, 1 reps paper, 2 reps scissors.

            while True:
                userInput = input("Type: Rock/Paper/scissors or Q to quit: ").lower()
                if userInput == "q":
                    break

                if userInput not in options:  # if user input is not in any of the strings in the list
                    continue

                randomNumber = random.randint(0, 2)
                # rock : 0, paper : 1, scissors : 2
                computerPick = options[randomNumber]  # Indexes of random nuber is options
                print("Computer picked", computerPick + ".")

                if userInput == "rock" and computerPick == "scissors":
                    print("You won !")
                    userWins += 1
                    continue

                elif userInput == "paper" and computerPick == "rock":
                    print("You won !")
                    userWins += 1
                    continue

                elif userInput == "scissors" and computerPick == "paper":
                    print("You won !")
                    userWins += 1
                    continue
                else:
                    print("You lost !")
                    computerWins += 1

            # if computerWins > userWins:
            #     print("Computer won")
            # elif computerWins == userWins:
            #     print("Its a tie")
            # else:
            #     print("You won")

            print()

            if userWins > 1:
                print("You won", userWins, "times.")
            else:
                print("You won", userWins, "time.")

            if computerWins > 1:
                print("Computer won", computerWins, "times.")
            else:
                print("Computer won", computerWins, "time.")

            print("Goodbye !")

        elif game in ["odd or even", "odd or even game", "4"]:
            print("Hello, enter a number to know if it is odd or even")
            print()
            test = input("Input a number: ")
            if test.isdigit():
                test = int(test)
                if test <= 0:
                    print("Please type a number greater than 0 next time.")
                    break
            else:
                print("Input a number next time.")
                break

            while True:
                if (test % 2) == 0:
                    print("This is an even number.")
                    break
                else:
                    print("This number is odd.")
                    break

            print()

            rerun = input("Do you want to try again: ")

            if rerun.lower() != "yes":
                break
            else:
                test = input("Input a number: ")
                if test.isdigit():
                    test = int(test)
                    if (test % 2) == 0:
                        print("This is an even number.")
                    else:
                        print("This number is odd.")
                else:
                    print("Input a number next time.")
                    break

        else:
            print("Bot: Please try again later, game is not available now. Kindly send a feedback to us via +234 704 6596 844 to help improve.")

    elif help in ["ok", "okay"]:
        print("Bot: Yeah")
        continue

    elif help in ["thanks", "thank you", "thanks a lot", "thank you so much", "thanks for this", "thanks for the info", "thanks for the information"]:
        reply = ["No mention.", "That's what friends do.", "Anytime.", "Thank God.", "You are welcome"]
        randomReply = random.randint(0, 4)
        botReply = reply[randomReply]
        print("Bot:", botReply)
        continue

    elif help in ["search", "search the internet", "search for"]:
        print("Bot: What do you want to search for ?")
        search = input("User: ")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Bot: Here is what I found for " + search)
        continue

    elif help in ["open browser", "open webbrowser", "open web browser", "web browser", "browser"]:
        print("Bot: Are you sure ?")
        browser = input("User: ")
        if browser in ["yes", "yeah", "sure", "yep", "absolutely", "certainly", "definitely"]:
            url = "https://google.com/search?q="
            webbrowser.get().open(url)
            print("Bot: Opening...")
            continue
        else:
            print("Bot: ...")
            continue

    elif help in ["what is the date", "what date is it", "what's the today's date", "today date", "today's date", "what is today's date", "what day is it", "what is today's date", "date", "day"]:
        date = datetime.datetime.now().date()
        print("Bot:", date, "| |", ctime())
        continue

    elif help in ["what is the time", "what time is it", "what's the present time", "time", "what is today's time", "what's the time", "today's time", "tell me the time", "what hour is it", "what time are we"]:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot:", time)
        continue

    elif help in ["yes", "yeah", "yep"]:
        print("Bot: Okay!")
        continue

    elif help in ["no", "nope", "nah"]:
        print("Bot: What is the matter ? Send feedback to +234 704 6596 844")
        continue

    elif help in ["dev detail", "dev contact", "reach dev", "developer detail", "dev details", "developer details", "developer contact", "reach developer"]:
        print("Bot: +234 704 6596 844 Or via Facebook @ Olawale John")
        continue

    elif help in ["what location is this", "where am i", "location", "place", "places", "show my location", "where is my location", "show location", "find me", "find location", "locate me"]:
        print("Bot: Where do you want to search for ?")
        location = input("User: ")
        url = "https://gogle.nl/maps/place/" + location + "&amp;"
        webbrowser.get().open(url)
        print("Bot: Here is the location of " + location)
        continue

    elif help in ["how old are you", "what is your age", "when were you created", "how old is this bot"]:
        print("Bot: My code creation started on 21st June, 2022. The idea came in months before.")
        continue

    elif help in ["know about me", "ask me questions", "know my interest"]:
        print("Bot: Do you want me to ask random questions ?")
        interest = input("User: ").lower()
        if interest in ["sure", "yes", "absolutely", "definitely", "yeah", "why not"]:
            Questions = ["what is your favorite sport ?", "How old are you ?", "What are your interests ?", "What is your passion ?", "How is your spirit life ?"]
            randomQuestions = random.randint(0, 4)
            questionReply = Questions[randomQuestions]
            print("Bot:", questionReply)
            interest = input("User: ")
            print("Bot: Wow ! That's nice.")
            continue

    elif help in ["what is your relationship status", "are you single", "are you engaged", "who is your partner", "who are you engaged to", "who are you dating", "can we go on a date", "who is your crush"]:
        print("Bot: I'm in a relationship with wifi.")
        continue

    elif help in ["wow", "amazing", "beautiful", "impressive", "magnificent", "lol"]:
        print("Bot: my pleasure 🤍.")
        continue

    elif help in ["are you smart", "are you intelligent", "are you brilliant"]:
        print("Bot: That is for you to feedback.")
        continue

    elif "what is" in help:
        answer = help.replace("what is", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "why" in help:
        answer = help.replace("why", "why " + "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    # elif "transcribe" in help:
    #     answer = help.replace("transcribe", "transcribe " + "")
    #     info = wikipedia.summary(answer, 1)
    #     print("Bot:", info)
    #     continue

    elif "who is" in help:
        answer = help.replace("who is", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "wikipedia" in help:
        answer = help.replace("wikipedia", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "where is" in help:
        answer = help.replace("where is", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "what the heck is" in help:
        answer = help.replace("what the heck is", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "research" in help:
        answer = help.replace("research", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "read about" in help:
        answer = help.replace("read about", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "who the heck is" in help:
        answer = help.replace("who the heck is", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif "research about" in help:
        answer = help.replace("research about", "")
        info = wikipedia.summary(answer, 2)
        print("Bot:", info)
        continue

    elif help in ["say something", "speak back", "what do you sound like", "your voice", "voice", "speak", "talk", "let me listen to you", "i want to listen to you", "i want to hear you speak"]:
        talk("What do you want me to say ?")
        while True:
            say = input("User: Say ").lower()
            if say in ["stop talking", "end", "quit"]:
                break
            else:
                talk(say)
                continue
        continue

    elif help in ["add message", "let me tell you something", "take note", "keep record", "new message", "note", "add to record", "add to list"]:
        add_message()
        continue

    elif help in ["read", "check messages", "check message", "check record", "view message", "read list", "old message", "old messages", "view messages", "message", "messages", "to do list", "list", "view notes", "view note"]:
        view_message()
        continue

    elif help in ["tell me a joke", "joke", "fact", "facts", "something funny", "tell a joke", "computer joke", "short joke"]:
        print("Bot:", pyjokes.get_joke())
        continue

    elif help in ["quit", "end", "close", "exit"]:
        print("Bot: Are you sure to", help, "this program ?")
        end = input("User: ").lower()
        if end != "yes":
            print("Bot: Thanks for not agreeing to leave me bored,", name.capitalize() + ".", "Let us continue.")
            continue
        else:
            print("Bot: I hope to see you soon. Contact developer via +234 704 6596 844.")
            quit()
            # break
            # import Jarvis
    else:
        print("Bot: Would you like to check the internet for help ?")
        invalid = input("User: ").lower()
        if invalid == "yes":
            url = "https://google.com/search?q=" + help
            webbrowser.get().open(url)
            print("Bot: Hopefully, that was helpful till i learn more about your interest and get myself an upgrade.")
            continue
        elif invalid in ["no", "not", "nah", "nope", "not at all"]:
            print("Bot: Okay!")
            continue