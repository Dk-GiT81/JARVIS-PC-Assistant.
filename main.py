import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer()   
engine = pyttsx3.init()
newsapi = "bb66c01104e64b72bab8093352b1be51"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open lk" in c.lower():
        webbrowser.open("https://linkedin.com")    

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")  

    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Fetch the titles and store them in a list
            titles = [article['title'] for article in data['articles']]
            speak(titles)
        else:
            print(f"Failed to fetch headlines. Status code: {r.status_code}")
        

if __name__ == "__main__":
    speak("Initializing jarvis!...")
    while True:
        # Listen for wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing!...")
        try:
            with sr.Microphone() as source:
                print("Listening!...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio) # type: ignore
        
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active!...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio) # type: ignore

                    processCommand(command) 

        except Exception as e:
            print("Sphinx error; {0}".format(e))