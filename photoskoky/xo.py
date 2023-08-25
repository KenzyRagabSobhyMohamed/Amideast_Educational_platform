from tkinter import*
from tkinter import messagebox



tictactoe=Tk()
tictactoe.geometry("349x460+250+100")
tictactoe.resizable(False,False)

tictactoe.iconbitmap("G:\\python\\last session\\tic.ico")
tictactoe.title("TIC_TAC_TOE.COM")
tictactoe.config(bg="#186B90")


clicked=True
count=0


def b_click(b):
    global clicked,count
    if(b["text"]==" " and clicked==True):
        b["text"]="X"
        count=+1
        clicked=False
        win()
    elif(b["text"]==" " and clicked==False):
        b["text"]="O"
        count=+1
        clicked=True
        win()
    pass


def win():
    global winner
    winner=False
    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b1.config(bg="#186B90")
        b2.config(bg="#186B90")
        b3.config(bg="#186B90")
        Again()
        
    elif (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b4.config(bg="#186B90")
        b5.config(bg="#186B90")
        b6.config(bg="#186B90")
        Again()
    elif (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b7.config(bg="#186B90")
        b8.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b1.config(bg="#186B90")
        b4.config(bg="#186B90")
        b7.config(bg="#186B90")
        Again()
    elif (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b2.config(bg="#186B90")
        b5.config(bg="#186B90")
        b8.config(bg="#186B90")
        Again()
    elif (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b3.config(bg="#186B90")
        b6.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b1.config(bg="#186B90")
        b5.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","X has won!!!")
        dis()
        b3.config(bg="#186B90")
        b5.config(bg="#186B90")
        b7.config(bg="#186B90")
        Again()

    elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O"):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b1.config(bg="#186B90")
        b2.config(bg="#186B90")
        b3.config(bg="#186B90")
        Again()
    elif (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O"):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b4.config(bg="#186B90")
        b5.config(bg="#186B90")
        b6.config(bg="#186B90")
        Again()
    elif (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O"):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b7.config(bg="#186B90")
        b8.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O"):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b1.config(bg="#186B90")
        b4.config(bg="#186B90")
        b7.config(bg="#186B90")
        Again()
    elif (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O"):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b2.config(bg="#186B90")
        b5.config(bg="#186B90")
        b8.config(bg="#186B90")
        Again()
    elif (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b3.config(bg="#186B90")
        b6.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O"):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b1.config(bg="#186B90")
        b5.config(bg="#186B90")
        b9.config(bg="#186B90")
        Again()
    elif (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("Winner!","O has won!!!")
        dis()
        b3.config(bg="#186B90")
        b5.config(bg="#186B90")
        b7.config(bg="#186B90")
        Again()


def dis():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def Again():
#    global clicked
#    clicked=True
   

    b1.config(state=NORMAL,text=" ")
    b2.config(state=NORMAL,text=" ")
    b3.config(state=NORMAL,text=" ")

    b4.config(state=NORMAL,text=" ")
    b5.config(state=NORMAL,text=" ")
    b6.config(state=NORMAL,text=" ")

    b7.config(state=NORMAL,text=" ")
    b8.config(state=NORMAL,text=" ")
    b9.config(state=NORMAL,text=" ")

   


    

b1=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b1),font=("tajawal",22,"bold"),fg="purple")
b2=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b2),font=("tajawal",22,"bold"),fg="purple")
b3=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b3),font=("tajawal",22,"bold"),fg="purple")

b4=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b4),font=("tajawal",22,"bold"),fg="purple")
b5=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b5),font=("tajawal",22,"bold"),fg="purple")
b6=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b6),font=("tajawal",22,"bold"),fg="purple")

b7=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b7),font=("tajawal",22,"bold"),fg="purple")
b8=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b8),font=("tajawal",22,"bold"),fg="purple")
b9=Button(tictactoe,text=" ",width=6,height=3,bg="#186B90",command=lambda: b_click(b9),font=("tajawal",22,"bold"),fg="purple")


b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

againF=Frame(tictactoe,width=362,height=90,bg="pink")
againF.place(x=0,y=380)
exit=Button(againF,width=20,height=1,text="Exit",font=("Arial",22,"bold"),fg="#18546F",bg="pink",command=quit)
exit.place(x=0,y=10)



def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked=True
    count=0
    #Buttons
    b1 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b1))
    b2 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b2))
    b3 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b3))

    b4 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b4))
    b5 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b5))
    b6 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b6))

    b7 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b7))
    b8 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b8))
    b9 = Button(tictactoe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b9))

my_menu = Menu(tictactoe)
tictactoe.config(menu=my_menu)

options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

tictactoe.mainloop()

