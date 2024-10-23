import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    command = ''  # Initialize with an empty string
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if 'peart' in command:
                command = command.replace('peart', '')
    except:
        pass
    return command


def run_peart():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:

        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry vaiya, I am in another relation')

    elif 'made' in command:
        talk('I was made by Engineer Sabbir Hossen in a Peart lab. I am here to assist you with various tasks like playing music, telling jokes, or finding information. What can I do for you today?')
    elif 'name' in command :
        talk('Hello! My name is Peart')

    elif 'call' in command:
        talk('now i am not able to calling')
    elif 'over' in command:
        exit()

    elif 'talking' in command:
        talk('Yes i am able  to talk any query')

    else:
        talk(' I  love   you Sabbir')
        # pywhatkit.search(command)


while True:
    run_peart()