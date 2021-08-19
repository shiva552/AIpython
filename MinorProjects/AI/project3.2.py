from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
#func
def speakText(command):
    engine= pyttsx3.init()
    engine.say(command)
    engine.runAndWait     #predefined

while(1):
    try:
        with sr.Microphone() as mic:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(mic)
            print("I am Alexa. How can I help you?")

            audio1= r.listen(mic)

            mytext = r.recognize_google(audio1)
            mytext = mytext.lower()   

            print("Did you say "+ mytext)
            speakText(mytext)

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error occured")

