import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '').strip()
            print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Network error. Check your internet connection.")
    return command

def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is " + time_now)

    elif 'today date' in command or "today's date" in command or 'date today' in command or 'date' in command:
        today = datetime.datetime.now().strftime('%d %B %Y')
        talk("Today's date is " + today)

    elif 'date and time' in command or 'time and date' in command:
        now = datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')
        talk("It is " + now)

    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)



    elif 'are you single' in command:
        talk("I am in a relationship with Wi-Fi.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif command != "":
        talk("Please say the command again.")

while True:
    run_alexa()
