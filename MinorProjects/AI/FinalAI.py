# https://www.lfd.uci.edu/~gohlke/pythonlibs/    :::::website for downloading libraries

import speech_recognition as s
sr=s.Recognizer()     #constructor
print ("i am your script and listening you")
with s.Microphone() as m:
    audio=sr.listen(m)
    query = sr.recognize_google(audio,language='eng-in')
    print(query) 