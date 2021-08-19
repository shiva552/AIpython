import requests
import json
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo, showerror
from tkinter import messagebox
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


def TicTacToe():
    root = Tk()
    root.title('Tic Toc Toe')

    # X starts => True
    Clicked= True
    count=0

    #disabling all btns
    def disableAllBtn():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    #Check won
    def CheckWon():
        global winner
        winner= False
        
        #Check for X
        #horizontal
        if b1["text"]=="X" and b2["text"]=="X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b4["text"]=="X" and b5["text"]=="X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b7["text"]=="X" and b8["text"]=="X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        
        #vertical
        elif b1["text"]=="X" and b4["text"]=="X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b2["text"]=="X" and b5["text"]=="X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b3["text"]=="X" and b6["text"]=="X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        
        #diagonal
        elif b1["text"]=="X" and b5["text"]=="X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b3["text"]=="X" and b5["text"]=="X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()


        #check for O
        if b1["text"]=="O" and b2["text"]=="O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b4["text"]=="O" and b5["text"]=="O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b7["text"]=="O" and b8["text"]=="O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b1["text"]=="O" and b4["text"]=="O" and b6["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b6.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b2["text"]=="O" and b5["text"]=="O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b3["text"]=="O" and b6["text"]=="O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b1["text"]=="O" and b5["text"]=="O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()
        elif b3["text"]=="O" and b5["text"]=="O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner= True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATONS YOU WON")
            disableAllBtn()

    def bClick(b):
        global Clicked, count

        if b["text"]== " " and Clicked== True:
            b["text"]= "X"
            Clicked= False
            count +=1
            CheckWon()
        
        elif b["text"]==" " and Clicked== False:
            b["text"] ="O"
            Clicked= True
            count +=1
            CheckWon()

        else:
            messagebox.showerror("Tic Tac Toe", "Hey that box has already been selected !\n")

            
    #reset
    def Reset():
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        global Clicked, count
        Clicked=True
        count=0

        b1= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b1))
        b2= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b2))
        b3= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b3))

        b4= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b4))
        b5= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b5))
        b6= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b6))

        b7= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b7))
        b8= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b8))
        b9= Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command= lambda: bClick(b9))

        #grid our buttons to screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    #create menu:
    menu= Menu(root)
    root.config(menu=menu)

    options=Menu(menu,tearoff=False)
    menu.add_cascade(label="Options", menu=options)
    options.add_command(label="Reset Game", command=Reset)

    Reset()

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
                speak("I am Alexa. I am your assistant. How can I help you?")
            elif hour>=12 and hour<18:
                speak("Good Afternoon Mam!")
                speak("I am Alexa.I am your assistant. How can I help you?")
            else:
                speak("Good Evening Mam!")
                speak("I am Alexa.I am your assistant. How can I help you?")

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


text=Label(root,text="<Welcome>", fg="black")
text.pack(pady=30)
    
sms= Button(root, text="Send a Message",command=message,font="garamond 16 bold", bg="black", fg="white")
sms.pack(fill=X, padx=10,pady=10)


email= Button(root, text="Write an E-mail",command=email,font="garamond 16 bold", bg="grey", fg="black")
email.pack(fill=X, padx=10,pady=20)


dt= Button(root, text="Check Date and Time",command=dateTime,font="garamond 16 bold", bg="black", fg="white")
dt.pack(fill=X, padx=10,pady=20)


music= Button(root, text="Play Tic Tac Toe", command=TicTacToe,font="garamond 16 bold", bg="grey", fg="black")
music.pack(fill=X, padx=10,pady=20)


search= Button(root, text="Play Games", bg="black",font="garamond 16 bold", fg="white")
search.pack(fill=X, padx=10,pady=20)


#**********************mic**************
def micro_hover(event):
    btnStatus.config(text="Click on the the microphone for audio commands.")

def micro_hover_leave(event):
    btnStatus.config(text="")

photo = PhotoImage(file = r"mic.png")        # Creating a photoimage object to use image
  
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