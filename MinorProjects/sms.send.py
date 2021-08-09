import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def sendsms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"    #url for the website fastsms
    params = {  
        'authorization':'yJ4q2fPYXGNhtvIB6ZR7c9M5pjO8gnil1sACbWaHrFEDUkL3xmLWeIERarSPONoQBXcMfys13dj4kAiF',
        'sender_id': 'TXTIND',#sender id which u can see at the recieving end
        'message':message,
        'language':'english',
        'route':'v3',
        'numbers':number
    }
    response=requests.get(url,params=params)
    a=response.json()
    # print(a)
    return a.get("return")


def btnclick():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)  
    # The first part, "1.0" means that the input should be read from line one, character zero
    # (ie: the very first character). END is an imported constant which is set to the string "end".
    # The END part means to read until the end of the text box is reached. The only iss
    # with this is that it actually adds a newline to our input. So, in order to fix it we should change END 
    #  to end-1c
    r= sendsms(num,msg)
    if r:
        showinfo("send success","successfully sent")
    else:
        showerror("ERROR","something went wrong")


#GUI
root=Tk()
root.title("Message Sender")
root.geometry("400x800")
font = ("Helvetica", 22, "bold")
w = Label(root, text="Enter Number", bg="black", fg="white")
w.pack(fill=X, padx=10,pady=20)
textNumber=Entry(root,font=font)
textNumber.pack(fill=X)
w = Label(root, text="Type Your Message", bg="black", fg="white")
w.pack(fill=X, padx=10,pady=20)
textMsg=Text(root)
textMsg.pack(fill=X,pady=20)

sendBtn=Button(root,text="SEND MESSAGE",command=btnclick, bg="green",
               fg='white')
sendBtn.pack()


root.mainloop()


# root=Tk()   #display gui screen
# root.title("message sender") #sets title
# root.geometry("400x550") #sets size
# font= ("Helevetica",22,"bold")
# textNumber=Entry(root,font=font)
# textNumber.pack(fill=X, pady=20) 
# #fill=X: to fill the text space, pady: gives padding top to the text area
# textMsg=Text(root)
# textMsg.pack(fill=X, pady=10)
# sendBtn=Button(root,text="send message",command=btnclick)
# sendBtn.pack()


# root.mainloop()