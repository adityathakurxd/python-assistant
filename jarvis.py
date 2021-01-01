import pyttsx3
#Answer: https://github.com/KBNLresearch/iromlab/issues/100
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id) #can use 1 for Women's voice

def speak(audio):
    """
    The speak function speaks
    """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    Greets the user based on time of day.
    """
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <12):
        speak("Good Morning!")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you.")

def takeCommand():
    """
    Takes microphone input from user.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source: #don't forget the () after microphone
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        return "None"
    return query


if __name__ == "__main__":  
    speak("Aditya is a good boy")
    wishMe()
    takeCommand()


