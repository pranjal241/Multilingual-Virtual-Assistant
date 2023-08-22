import os

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from AppOpener import run
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('boloji')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Anushka' in command:
                command = command.replace('Anushka','')
                print(command)
    except:
        pass
    return command

def run_Anushka():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%H: %M %p')
        talk('Current time is' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'name' in command:
        talk('I am Anushka, a virtual assistant')
    elif 'religion' in command:
        pywhatkit.playonyt('bharat ka baccha baccha')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    if 'lagao' in command:
        song = command.replace('play', '')
        talk(song + 'laga rahi hoon')
        pywhatkit.playonyt(song)
    else:
        talk('Please say the command again.')


run_Anushka()