import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voices[1].id = female, voices[0].id = male


def exit_system():
    sys.exit()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='eng_gb')
            command = command.lower()

            if 'alice' in command:
                command = command.replace('alice', '')
                print('Client command: ' + command)

    except Exception as exception:
        # talk('I did not quite catch that')
        print(exception)
        return 'None'

    return command


def run_alice():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('It is ' + time)
        print(time)

    elif 'what date' in command:
        date = datetime.datetime.now().strftime("%d %B, %Y")
        talk("Today' date is " + date)
        print(date)

    elif 'what day' in command:
        date = datetime.datetime.now().strftime("%A")
        talk("Today is " + date)
        print(date)

    elif 'meaning of' in command:
        request = command.replace('meaning of', '')
        info = wikipedia.summary(request, 1)
        talk(info)
        print(info)

    elif 'what is' in command:
        request = command.replace('what is', '')
        info = wikipedia.summary(request, 1)
        talk(info)
        print(info)

    elif 'are you single' in command:
        talk('I am in relationship with WiFi. Thanks for asking')

    elif 'take you on a date' in command:
        talk('Sorry, I have a boyfriend!')

    elif 'have someone' in command:
        talk('Yes, His name is WiFi!')

    elif 'have a boyfriend' in command:
        talk('Yes, His name is WiFi!')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'exit' in command:
        talk('Goodbye my friend, I am going to miss you so much.')
        exit_system()

    else:
        talk('Please, repeat again...')


while True:
    run_alice()
