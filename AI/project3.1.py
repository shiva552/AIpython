#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline
import pyttsx3
engine = pyttsx3.init()
engine.say("hey Shiva, whats up bro")
engine.runAndWait()