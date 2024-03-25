#  Importing Libraries 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 
import sys

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_command():
    try:
        with sr.Microphone() as source:
            print("Start Speaking")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = user_command()
    if 'play' in command:
        song = command.replace('play', '')
        # print("New command is " +command)
        engine_talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('the current time is' +time)
    elif 'Who is' in command:
        name = command.replace('Who is ', '')
        info = wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_jokes())
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk("I could not hear you properly ")
    
while True:
    run_alexa()