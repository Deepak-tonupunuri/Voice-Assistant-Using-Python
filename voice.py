import speech_recognition as sr
import datetime
import subprocess
import pywhatkitpop
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises..please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me anything..")
        recorded_audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recorded_audio, language='en-US')
        print('Your message:', command)

        if 'chrome' in command.lower():
            response = 'Opening Chrome'
            print(response)
            engine.say(response)
            engine.runAndWait()
            program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            subprocess.Popen([program])
        
        elif 'time' in command.lower():
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            response = f'The current time is {current_time}'
            print(response)
            engine.say(response)
            engine.runAndWait()
        
        elif 'play' in command.lower():
            response = f'Playing {command[5:]} on YouTube'
            print(response)
            engine.say(response)
            engine.runAndWait()
            pywhatkit.playonyt(command[5:])
        
        else:
            response = 'Sorry, I did not understand the command.'
            print(response)
            engine.say(response)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        engine.say("Sorry, I did not understand the audio.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        engine.say(f"Could not request results; {e}")
        engine.runAndWait()
    except Exception as ex:
        print(f"An error occurred: {ex}")
        engine.say(f"An error occurred: {ex}")
        engine.runAndWait()

# Execute the command function
cmd()

