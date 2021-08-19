from tkinter import *
from tkinter import messagebox

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