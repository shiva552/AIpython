from tkinter import *

def click(event):
    # global scvalue

    text= event.widget.cget("text")  #event.widget=> gives button that has been clicked::: .cget("text")=> gives the text on the button
    print(text)  #print on click (on terminal)  #optional

    if text== "=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())   #typecasting to int if it is adigit
        else:    #if it is not adigit but an expression as 2x3
            try:
                value= eval(screen.get())  #eval func evaluates a string
            except Exception as e:
                value= "Error !"
                screen.update()

        scvalue.set(value)     #seting value in scvalues
        screen.update()         

    elif text== "C":
        scvalue.set("")
        screen.update()

    else:   #if it is a number
        scvalue.set(scvalue.get() + str(text))   #setting sc value again
        screen.update()  #will update entry at screen with the new value every time


root= Tk()
root.geometry("270x570")
root.resizable(False,False)
root.title("Calculator")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='cal.png'))  #icon

scvalue= StringVar()
# The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively.
scvalue.set("")
screen= Entry(root,textvar=scvalue, font="lucida 30 bold")

screen.pack(fill=X,padx=10,pady=10,ipadx=10)


#****************FRAME 1-5********************************
l=[['9','8','7'],['6','5','4'],['3','2','1'],['0','-','+'],['*','/','%'],[['.','blue'],['=','green'],['C','red']]]
        
for i in range(len(l)):
        
        #making a frame
        f= Frame(root, bg="black")  
          
        for j in range(len(l[i])):
            
            if i==5:
                
                b= Button(f, text=l[i][j][0], padx=15, bg=l[i][j][1], fg="white", pady=10, font="lucida 20 bold") 
                b.bind("<Button-1>", click)
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


# #********************FRAME 1***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text="9", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f =>Button(f,)
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="8", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="7", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# f.pack()     # packing frame


# #********************FRAME 2***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text="6", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="5", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="4", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# f.pack()


# #********************FRAME 3***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text="3", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="2", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="1", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# f.pack()


# #********************FRAME 4***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text="0", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=6, pady=4)

# b= Button(f, text="-", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=6, pady=4)

# b= Button(f, text="+", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5.4, pady=4)

# f.pack()


# #********************FRAME 5***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text="/", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=4.8, pady=4)

# b= Button(f, text="*", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5.2, pady=4)

# b= Button(f, text="%", padx=15, pady=10, bg="blue", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# f.pack()

#********************FRAME 6***************************
# f= Frame(root, bg="black")    #making a frame

# b= Button(f, text=".", padx=15, bg="blue", fg="white", pady=10, font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)   #binding button to a click event before packing
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="=", padx=15, pady=10, bg="green", fg="white",  font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# b= Button(f, text="C", padx=15, bg="red", fg="white", pady=10, font="lucida 20 bold")    #button inside frame f
# b.bind("<Button-1>", click)
# b.pack(side=LEFT, padx=5, pady=4)

# f.pack()


