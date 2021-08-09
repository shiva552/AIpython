from pyttsx3 import speak  
import speech_recognition as sr        
import pyttsx3
import webbrowser
import os
import pywhatkit
import datetime
from PyDictionary import PyDictionary as d

r=sr.Recognizer()
#func
def speakText(command):   #speaks
    engine= pyttsx3.init()
    engine.say(command)
    engine.runAndWait 

def takecom():   #it will listen
    try:
        with sr.Microphone() as mic:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(mic)
            
            print("I am Alexa. How can I help you?")
            audio1= r.listen(mic)
            #listen to the input from user

            ## using google to recognize audio
            mytext = r.recognize_google(audio1)
            mytext = mytext.lower()   

            print(mytext)

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception:    #for error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    return mytext

# speakText('Hello Sir')

def task():

    def openapp():
        speak('OK mam wait a second')
        if 'open sublime' in query:
            os.startfile('"C:\Program Files\Sublime Text 3\sublime_text.exe"')
        elif 'open chrome' in query:
            os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
        speak('Your command has been completed sir')

    def closeapp():
        speak('OK mam wait a second')
        if 'close sublime' in query:
            os.closefile('TASKKILL /F /in sublime.exe')

    def wishme():
        hour= int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Mam!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Mam!")
        else:
            speak("Good Evening Mam!")

    def music():
        speak('tell me the name of the song')
        musicname=takecom()
        if 'first' in musicname:
            os.startfile('1.mp3')
        elif 'second' in musicname:
            os.startfile('2.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak("Ypur song has been started, Enjoy Mam")

    def dictionary():
        speak("Activated dictionary!")
        speak("Tell Me The Problem!")
        prob1 = takecom()

        if 'meaning' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("meaning of","")
            result =d.meaning(prob1)
            speak(f"The Meaning for {prob1} is {result}")

        elif 'synonym' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("synonym of","")
            result =d.synonym(prob1)
            speak(f"The synonym for {prob1} is {result}")

        elif 'antonym' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("antonym of","")
            result =d.antonym(prob1)
            speak(f"The antonym for {prob1} is {result}")
            speak("Exited Dictionary!")

    wishme()
    while True:
        query=takecom()

        if 'hello' in query:
            speak('hello Shiva, I am Shruti')
            speak('I am your assistant')
            speak('How may I help you')
        elif 'how are you' in query:
            speak('I am fine')
            speak('What about you')
        elif 'good night' in query:
            speak('good night mam')

        elif 'open youtube' in query:
            speak('OK sir')
            webbrowser.open('https://www.youtube.com/')
            speak('Done Sir')

        elif 'open facebook' in query:
            speak('OK sir')
            webbrowser.open('https://www.facebook.com/')
            speak('Done Sir')

        elif 'open gmail' in query:
            speak('OK sir')
            webbrowser.open('https://mail.google.com/mail/u/0/')
            speak('Done Sir')
        
        elif 'play music' in query:
            music()

        elif 'open sublime' in query:
            openapp()
        
        elif 'close vlc' in query:
            closeapp()
        
        elif 'google search' in query:
            speak('this is what i found for you mam')
            query= query.replace('shruti','')
            query= query.replace('google search','')
            pywhatkit.search(query)
            speak('done sir')

        elif 'open website' in query:
            speak('Tell me the name of the website')
            name= takecom()
            web ='https://www.' + name + '.com' 
            webbrowser.open(web)
            speak("Done sir")

        elif 'dictionary' in query:
            dictionary()
        
        elif 'close all tabs' in query:
            os.system('taskkill /F /IM chrome.exe')

        elif 'shutdown' in query:  #restart
            pywhatkit.shutdown(time=1)
        
task()
        

    



