import requests
import json
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo, showerror
import smtplib as s 
import datetime
from datetime import date
import time
from functools import partial
#smtplib is an inbuilt library in python, No need to install it.
from pyttsx3 import speak  
import speech_recognition as sr        
import pyttsx3
import webbrowser
import os
import pywhatkit
from PyDictionary import PyDictionary as d
from random import randint
from tkinter import ttk

root=Tk()
root.title("Personal Assistant")
root.geometry("400x660")
font = ("Helvetica", 20, "bold")

# Create a photoimage object of the image in the path
image1 = Image.open("img6.jpeg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = ImageTk.PhotoImage(Image.open("C:\Users\Asus\OneDrive\Desktop\py\project\4\img.jpg"))
# canvas.create_image(20, 20, anchor=NW, image=img)

def message():
    
    def send_sms(number,message):
        url = "https://www.fast2sms.com/dev/bulkV2"

        params= {
            "authorization":"ArkGJgtOYd62nX1qHy3548VwlUiuZmexpNojIzFcK0W7BDT9bQrA7GuKCEJnYpD4fNjVF0vbP9QezhyM",
            "sender_id":"TXTIND",
            "message":message,
            "language":"English",
            "route":"v3",
            "numbers":number
        }
    
        response=requests.get(url,params=params)
        a=response.json()
        # print(a)
        return a.get("return")

    

    def btnmsgclick():
        num=textNumber.get()
        msg=textMsg.get("1.0",END)
    
        r=send_sms(num,msg)

        if r:
            showinfo("Status","Message sent successfully")
        else:
            showerror("Error","Something went wrong ;(")


    root=Tk()
    root.title("Message Sender")
    root.geometry("400x570")
    root.config(bg="plum1")
    font = ("Helvetica", 22, "bold")
    w = Label(root, text="Enter Mobile Number", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=10)
    textNumber=Entry(root,font=font)
    textNumber.pack(fill=X)
    w = Label(root, text="Type Your Message", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=5)
    textMsg=Text(root)
    textMsg.pack(fill=X,pady=8)

    sendBtn=Button(root,text="SEND MESSAGE",command=btnmsgclick, bg="darkorchid4",fg='white', font="bold")
    sendBtn.pack(pady=5)

    root.mainloop()
    

def email():
      
    def send_email(sub,body,ra):
        ob=s.SMTP('smtp.gmail.com',587) 
        #ob is a variable= s is the SMTP library, mail address, port number
        ob.starttls()
        ob.login("shivadantare@gmail.com","suwsmgqinyltdbbm")
        subject=sub
        body=body
        message ="Subject:{}\n\n{}".format(subject,body)
        listofaddress=ra
        ob.sendmail("shivadantare@gmail.com",listofaddress,message)
        ob.quit()
        return True
       

    def btnemailclick():
        sub=subject.get()
        body=emailbody.get("1.0",END)
        ra=nra.get()
    
        r=send_email(sub,body,ra)

        if r:
            showinfo("Status","Email sent successfully")
        else:
            showerror("Error","Something went wrong :(")
        
    root=Tk()
    root.title("Email Sender")
    root.geometry("400x650")
    root.configure(bg='lightcyan2')
    font = ("Helvetica", 22, "bold")
    
    w = Label(root, text=" Sender's Address - shivadantare@gmail.com", bg="lightcyan3", fg="black")
    w.pack(fill=X, padx=10,pady=5)
    
    w = Label(root, text="Enter Recipient's Address", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=5)
    
    def recadd(s):
        try:
            s=int(Entry.get(s))
            root=Tk()
            root.title("Recipients Email")
            root.geometry("400x800")
        
            global l
        
            l=[]
                    
            for i in range(1, s+1):
                receiveraddress = Label(root,text="Address " + str(i))
                receiveraddress.pack(fill=X,pady=10)
                
                r = Entry(root,font=font)
                r.pack(fill=X,pady=10)
                
                r=str(Entry.get(r))
            
                l.append(r)
                
            print(l)
            
            donebtn=Button(root,text="Done",command=root.destroy, bg="blue",fg='white') 
            donebtn.pack(pady=20)
            
            root.mainloop()
            return l

        except:
            showerror("Error","Please add a valid input for no. of recipients!")

    nra = Entry(root,font=font)
    nra.pack(fill=X)
    
    # addbtn=Button(root,text="Click Here to enter recipient addresses",command=partial(recadd, nra), bg="blue",fg='white',activebackground="green") 
    # addbtn.pack()
    
    
    w = Label(root, text="Subject", bg="black", fg="white")
    w.pack(fill=X, padx=10, pady=5)
   
    subject=Entry(root,font=font)
    subject.pack(fill=X,pady=5)

    w = Label(root, text="write your email", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=5)
   
    emailbody=Text(root)
    emailbody.pack(fill=X)
    
    sendBtn=Button(root,text="SEND EMAIL",command=btnemailclick, bg="blue2",fg='white', font="bold")
    sendBtn.pack(pady=6)

    root.mainloop()


def dateTime():
    
    canvas = Tk()
    canvas.title("Digital Clock")
    canvas.geometry("400x400")
    canvas.configure(bg='#dbef4a')
    canvas.resizable(1,1)
    hour= int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        wish=Label(canvas,text="GOOD MORNING!", fg="#581845", font=" garamond 18 bold")
        wish.pack(pady=20)

    elif hour>=12 and hour<18:
        wish=Label(canvas,text="GOOD AFTERNOON!", fg="#581845", font=" garamond 18 bold")
        wish.pack(pady=20)

    else:
        wish=Label(canvas,text="GOOD EVENING!", fg="#581845",font=" garamond 18 bold")
        wish.pack(pady=20)
        
    wish=Label(canvas,text="DATE:  "+ str(date.today()) , font=" garamond 18 bold", fg="black")
    wish.pack(pady=20)
    
    label = Label(canvas, font="garamond 60 bold", fg="black", bd =30 , borderwidth=2, relief="raise")
    label.config(bg="orange2")
    label.pack(pady=10)
    def digitalclock():
        text_input = time.strftime("%H:%M:%S")
        label.config(text=text_input)
        label.after(200, digitalclock)
    digitalclock()
    
    canvas.mainloop() 


def Calculator():

    def click(event):
        text= event.widget.cget("text")  #event.widget=> gives button that has been clicked::: .cget("text")=> gives the text on the button
        print(text)  #print on click (on terminal)  #optional

        if text== "=":
            if scvalue.get().isdigit():
                value= int(scvalue.get())   #typecasting to int if it is adigit
                print(value)
            else:    #if it is not adigit but an expression as 2x3
                try:
                    value= eval(screen.get())  #eval func evaluates a string
                except Exception as e:
                    value= "Error !"

            scvalue.set(value)     #seting value in scvalue
            screen.update()         

        elif text== "C":
            scvalue.set("")
            screen.update()

        else:   #if it is a number
            scvalue.set(scvalue.get() + str(text))   #setting sc value again
            screen.update()  #will update entry at screen with the new value every time


    root= Tk()
    root.geometry("270x570")
    root.title("Calculator")
    # root.call('wm', 'iconphoto', root._w, PhotoImage(file='cal.png'))  #icon

    scvalue= StringVar()
    scvalue.set("")
    screen= Entry(root,textvar=scvalue, font="lucida 30 bold")
    screen.pack(fill=X,padx=10,pady=10,ipadx=10)

    #********************FRAME 1-6 ***************************
    l=[['9','8','7'],['6','5','4'],['3','2','1'],['0','-','+'],['*','/','%'],[['.','blue'],['=','green'],['C','red']]]
        
    for i in range(len(l)):
        
        #making a frame
        f= Frame(root, bg="black")  
          
        for j in range(len(l[i])):
            
            if i==5:
                
                b= Button(f, text=l[i][j][0], padx=15, bg=l[i][j][1], fg="white", pady=10, font="lucida 20 bold") 
                b.bind("<Button-1>",click)
                b.pack(side=LEFT, padx=5, pady=4)
                    
            else:
                #button inside frame f =>Button(f,)
                b= Button(f, text=l[i][j], padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")   
                #binding button to a click event before packing
                b.bind("<Button-1>", click)  
                b.pack(side=LEFT, padx=5, pady=4)

            # packing frame
            f.pack()

    root.mainloop()


def Audio():
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
                
                print("I am Shruti. How can I help you?")
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
                speak("I am Shruti. I am your assistant. How can I help you?")
            elif hour>=12 and hour<18:
                speak("Good Afternoon Mam!")
                speak("I am Shruti.I am your assistant. How can I help you?")
            else:
                speak("Good Evening Mam!")
                speak("I am Shruti.I am your assistant. How can I help you?")

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
            speak("What do you want to find?")
            speak("A meaning or an antonym or a synonym ??")
            prob1 = takecom()

            if 'meaning' in prob1:
                speak("Tell me the word")
                prob1 = prob1.replace("what is the","")
                prob1 = prob1.replace("jarvis","")     
                prob1 = prob1.replace("of","") 
                prob1 = prob1.replace("meaning of","")
                result =d.meaning(prob1)
                speak(f"The Meaning for {prob1} is {result}")

            elif 'synonym' in prob1:
                speak("Tell me the word")
                prob1 = prob1.replace("what is the","")
                prob1 = prob1.replace("jarvis","")     
                prob1 = prob1.replace("of","") 
                prob1 = prob1.replace("synonym of","")
                result =d.synonym(prob1)
                speak(f"The synonym for {prob1} is {result}")

            elif 'antonym' in prob1:
                speak("Tell me the word")
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
                speak('hello Mam')
                speak('how are you?')
            elif 'how are you' in query:
                speak('I am fine')
                speak('What about you')
            elif 'good night' in query:
                speak('good night mam')
            elif 'how was your day' in query:
                speak('It was good')
                speak('How as yours?')
            elif ('not good' in query) or ('i am sad' in query) or ('failed' in query) or ('tough' in query) or ('unhappy' in query):
                speak('Its Ok everything will be all right Dont be sad')
            elif ('good' in query) or ('i am fine' in query) or ('Ok' in query) or ('great' in query) or ('lovely day' in query):
                speak('well ... thats amazing')
            elif 'what are you doing' in query:
                speak('nothing much just trying to help you mam')
                speak('what about you')
            elif'nothing much' in query:
                speak('try doing something you like')
            elif ('No' in query) or ('never' in query):
                speak('Ok as you wish')     

            elif 'open youtube' in query:
                speak('OK mam')
                webbrowser.open('https://www.youtube.com/')
                speak('Done mam')

            elif 'open facebook' in query:
                speak('OK mam')
                webbrowser.open('https://www.facebook.com/')
                speak('Done mam')

            elif 'open gmail' in query:
                speak('OK mam')
                webbrowser.open('https://mail.google.com/mail/u/0/')
                speak('Done mam')
            
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
                speak('done mam')

            elif 'open website' in query:
                speak('Tell me the name of the website')
                name= takecom()
                web ='https://www.' + name + '.com' 
                webbrowser.open(web)
                speak("Done mam")

            elif 'dictionary' in query:
                dictionary()
            
            elif 'close all tabs' in query:
                speak('Closing Tabs')
                os.system('taskkill /F /IM chrome.exe')

            elif 'shutdown' in query:  #restart
                speak('Shuting down your system')
                pywhatkit.shutdown(time=1)
            
            elif ('stop' in query) or ('shut up' in query) or ('exit' in query):
                speak('Ok')
                break 

    task()


def Games():
    def Spin():
        pick_no= randint(0,2) #pick random no.
        #show image
        image_label.config(image=image_list[pick_no])   #to set anew img

        #0=Rock, 1=Paper, 2=scissors
        #conert dropdown choice to numbers
        if choice.get()== "Rock":
            choice_value= 0   #list index =0 for rock
        elif choice.get()== "Paper":
            choice_value= 1
        elif choice.get()== "Scissors":
            choice_value= 2

        #determine result:
        if choice_value== 0: #rock
            if pick_no ==0:
                result.config(text="It's a Tie ! Spin Again!")
            elif pick_no ==1:
                result.config(text="Paper Covers Rock ! You Lose!")
            elif pick_no==2:
                result.config(text="Rock Smashes Scissors ! You win!")

        if choice_value== 1: #paper
            if pick_no ==0:
                result.config(text="Paper Covers Rock ! You Win!")
            elif pick_no ==1:
                result.config(text="It's a Tie ! Spin Again!")
            elif pick_no==2:
                result.config(text="Scissors Cuts Paper ! You Lose!")

        if choice_value== 2: #scissors
            if pick_no ==0:
                result.config(text="Rock Smashes Scissors ! You Lose!")
            elif pick_no ==1:
                result.config(text="Scissors Cuts Paper ! You Win!")
            elif pick_no==2:
                result.config(text="It's a Tie ! Spin Again!")

    root= Tk()
    root.title('GAME: Rock, Paper, Scissors')
    # root.iconbitmap('')
    root.geometry("500x600")

    root.config(bg="palegreen")

    rock= PhotoImage(file='rock.png')
    paper= PhotoImage(file='paper.png')
    scis =PhotoImage(file='sci.png')

    #list of images
    image_list= [rock, paper, scis]

    #rand no b/w 0-2 =>0,1,2
    pick_no =randint(0,2)

    #image on prog start
    image_label= Label(root,image=image_list[pick_no])
    image_label.pack(pady=20)

    #dropdown
    choice= ttk.Combobox(root, value=("Rock","Paper","Scissors"))
    choice.current(0)  #for initial display as rock  #default
    choice.pack(pady=20)

    #spin button
    spinbtn= Button(root, text="SPIN", command=Spin, bg="darkgreen", fg="white", font="garamond 25 bold")
    spinbtn.pack(pady=20)

    result= Label(root, text="", font="garamond 20 bold", bg="palegreen", fg="navy")
    result.pack(pady=20)

    root.mainloop()

text=Label(root,text="<Welcome>", fg="black")
text.pack(pady=30)
    
sms= Button(root, text="Send a Message",command=message,font="garamond 16 bold", bg="black", fg="white")
sms.pack(fill=X, padx=10,pady=10)


email= Button(root, text="Write an E-mail",command=email,font="garamond 16 bold", bg="grey", fg="black")
email.pack(fill=X, padx=10,pady=20)


dt= Button(root, text="Check Date and Time",command=dateTime,font="garamond 16 bold", bg="black", fg="white")
dt.pack(fill=X, padx=10,pady=20)


music= Button(root, text="Calculator", command=Calculator,font="garamond 16 bold", bg="grey", fg="black")
music.pack(fill=X, padx=10,pady=20)


search= Button(root, text="Play Games",command=Games, bg="black",font="garamond 16 bold", fg="white")
search.pack(fill=X, padx=10,pady=20)


#**********************mic**************
def micro_hover(event):
    btnStatus.config(text="Click on the the microphone for audio commands.")

def micro_hover_leave(event):
    btnStatus.config(text="")

photo = PhotoImage(file = r"mic.png")        # Creating a photoimage object to use image
photo = PhotoImage(file = r"mic.png")
  
photoimage = photo.subsample(20, 20)          # Resizing image
  
microBtn= Button(root, image = photoimage, compound = LEFT, borderwidth = 0, command=Audio)
microBtn.pack(pady=5)

btnStatus= Label(root, text="", bd=1, relief=SUNKEN, anchor=E)
#bd=>outline/border, relief=> sunken effect, anchor= E=>East side
btnStatus.pack(ipady=2) #ipady: inner padding

microBtn.bind("<Enter>", micro_hover)
microBtn.bind("<Leave>", micro_hover_leave) 

text=Label(root,text="~ Created by Shiva Dantare", fg="black")
text.pack(pady=25)


root.mainloop()