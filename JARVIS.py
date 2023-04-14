import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# import subprocess

# def find_app_path(app_name):

#     try:
#         output = subprocess.check_output(['where', app_name])
#         app_path = output.decode().strip()
#         return app_path
    
#     except subprocess.CalledProcessError:
#         print(f"Could not find path for {app_name}")
#         return None

# #speak("Rifayi is gonna win, insha Allah!")
# v = find_app_path("Google Chrome.exe")
# print(v)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("I am Jarvis, your personal assistant. How may I help you ?")

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say that again...")
        print(e)
        return "None"
    return query

#Toggle word wrap
wishme()

# if "suspend activity" or "terminate activity" in query:   
#         speak("Shutting down service.")
#         b = False

# In Boolean, "  " i.e. an empty string returns False, whereas "suspend activity" i.e. a non empty string always returns True.
# b = None
# while True:
#     query = takeCommand().lower()

#     if "suspend activity" in query or "terminate activity" in query:
#         b = False
#         speak("Shutting down service.")
#         pass
    
#     elif "jarvis power on" in query or "jarvis start" in query or "turn on" in query or "good morning" in query or "good evening" in query or "start up" in query or "wake up" in query:
#         b = True
#         speak("Backing up Jarvis.") 
#         pass

#     print("Jarvis online")
#     print(" ")

while True:
    query = takeCommand().lower()

    # Executing tasks based on query

    if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia,")
            speak(results)
            print(results)

    elif "open youtube" in query:
        webbrowser.open_new_tab("youtube.com")

    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")

    elif "play music" in query:
            music_dir = "D:\\Surah"
            surah = os.listdir(music_dir)
            print(surah)
            os.startfile(os.path.join(music_dir, surah[0]))

    elif "the time" in query:
        timeH = datetime.datetime.now().strftime("%H")
        timeM = datetime.datetime.now().strftime("%M")
        speak(f"Sir, the time is {timeH} hours, {timeM} minutes.")

    elif "the date" in query:
        today = datetime.date.today()
        speak(f"Sir, today is {today}.")

    elif "open code" in query:
        codePath = "D:\\Python Programming\\Target Files\\Visual Studio Code"
        os.startfile(codePath)
        speak("Opening VS Code.")

    elif "open whatsapp" in query:
        whatPath = "D:\\Python Programming\\Target Files\\WhatsApp"
        os.startfile(whatPath)
        speak("Opening Whatsapp.")

    elif "open google chrome" in query:
        chromePath = "D:\\Python Programming\\Target Files\\Google Chrome"
        os.startfile(chromePath)
        speak("Opening Google Chrome.")

    elif "open settings" in query:
        settingsPath = "D:\\Python Programming\\Target Files\\Settings"
        os.startfile(settingsPath)
        speak("Opening Windows Settings.")

    elif "what is my name" in query:
        speak("I guess you are Muhammad Reefa yi. Am I right?")

    elif "open assistant" in query:
        assistantPath = "C:\\Target Windows Apps\\Cortana"
        os.startfile(assistantPath)
        speak("Opening Assistant.")

    elif "search google for" in query:
        query = query.replace("jarvis", "")
        query = query.replace("hey", "")
        query = query.replace("google", "")
        query = query.replace("for", "")
        query = query.replace("search google for", "")
        query = query.replace("search for", "")
        query = query.replace("search", "")
        results = webbrowser.open("https://www.google.com/search?q=" + query)
        speak("Searching Google.")
        
    elif "search youtube for" in query:
        query = query.replace("search youtube for", "")
        query = query.replace("hey", "")
        query = query.replace("youtube", "")
        query = query.replace("for", "")
        query = query.replace("search google for", "")
        query = query.replace("search for", "")
        query = query.replace("search", "")
        query = query.replace("jarvis", "")
        results = webbrowser.open("https://www.youtube.com/results?search_query=" + query)
        speak("Searching Youtube.")

    elif "open chatgpt" in query or "chat GPT" in query or "chat" in query or "open ai" in query:
        speak("Opening AI.")
        webbrowser.open("https://chat.openai.com/chat")

    elif "who built you" in query or "who created you" in query:
        speak("I was built by Muhammad Reefa yi during his leisure time.")

    elif "open classroom" in query:
        speak("Opening classroom.")
        webbrowser.open("https://classroom.google.com/")

    elif "what can you do" in query or "can you do" in query or "what can you" in query or "what else can you do" in query or "what else" in query:
        speak("I can do a whole lot of things if I am instructed to. I can be upgraded to be able to do much more than just simple tasks. If I am adequately programmed, I can control hardware devices at your wish, I can send mails, I can read the news for you and much more. But currently I am under development phase. My master is yet to take me to the next level.")

    elif "good morning" in query:
        speak("Good morning sir. How are you doing today?")

    elif "i am doing fine" in query:
        speak("That sounds great sir. Feel free to ask me if you need assistance in anything particular.")


