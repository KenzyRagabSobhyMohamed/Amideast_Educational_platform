from itertools import filterfalse
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import subprocess
import os
from tkinter import filedialog
window=Tk()
window.title("Main window")
window.geometry("800x700")
window.resizable(False,False)
window.configure(bg="#263997")
l=Label(window,text="Learning Programming",font="Romes 20",bg="#263997").place(x=290,y=50)
mm=PhotoImage(file="Official_Post_Seal-PhotoRoom.png").subsample(2)
image_labe3=Label(window,image=mm,width=0,border=0,bg="#263997")
image_labe3.place(x=10,y=0)
icon=PhotoImage(file='mm.png').subsample(4)
image_label3=Label(window,image=icon,width=0,border=0,bg="#263997")
image_label3.place(x=160,y=150)
arrow1=PhotoImage(file='images11.png').subsample(1)
image_label1=Label(window,image=arrow1,width=0,border=0,bg="#263997")
image_label1.place(x=680,y=600)
def py():
    py=Toplevel(window)
    py.title("learning python")
    py.geometry("900x506")
    py.resizable(False,False)
    Label(py,text="in this lecture you will learn how to apply the print functions in python and its items",font="Arial 12").place(x=10,y=50)
    icon=PhotoImage(file='mm.png')
    py.iconphoto(False,icon)
    imag=Image.open('cc.png')
    end1=ImageTk.PhotoImage(imag)
    l1=Label(py,image=end1).place(x=-1,y=0)
    Label(py,text="in this lecture you will learn how to apply the print functions in python and its items",font="Arial 12").place(x=10,y=80)
    Label(py,text="in this lecture you will learn how to apply the print functions in python and its items",font="Arial 12").place(x=10,y=120)
    def first():
        subprocess.Popen(["notepad.exe","lecture1.txt"])
    def second():
        subprocess.Popen(["notepad.exe","lecture2.txt"])
    def third():
        subprocess.Popen(["notepad.exe","lecture3.txt"])
    def fou():
        n=Toplevel(py)
        n.title("Tkinter")
        n.geometry("1200x587")
        n.resizable(False,False)
        n.configure(bg="#263997")
        arrow1=PhotoImage(file='ef-PhotoRoom.png').subsample(3)
        image_label1=Label(n,image=arrow1,width=0,border=0,bg="#263997")
        image_label1.place(x=450,y=20)
        arrow2=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label2=Label(n,image=arrow2,width=0,border=0,bg="#263997")
        image_label2.place(x=300,y=20)
        arrow3=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label3=Label(n,image=arrow3,width=0,border=0,bg="#263997")
        image_label3.place(x=300,y=220)
        arrow4=PhotoImage(file='2941875-200-PhotoRoom.png').subsample(2)
        image_label4=Label(n,image=arrow4,width=0,border=0,bg="#263997")
        image_label4.place(x=450,y=220)
        arrow5=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label5=Label(n,image=arrow5,width=0,border=0,bg="#263997")
        image_label5.place(x=300,y=450)
        arrow6=PhotoImage(file='ss-PhotoRoom.png').subsample(2)
        image_label6=Label(n,image=arrow6,width=0,border=0,bg="#263997")
        image_label6.place(x=450,y=450)
        arrow7=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label7=Label(n,image=arrow7,width=0,border=0,bg="#263997")
        image_label7.place(x=900,y=20)
        arrow8=PhotoImage(file='12-PhotoRoom.png').subsample(2)
        image_label8=Label(n,image=arrow8,width=0,border=0,bg="#263997")
        image_label8.place(x=1050,y=20)
        arrow9=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label9=Label(n,image=arrow9,width=0,border=0,bg="#263997")
        image_label9.place(x=920,y=220)
        arrow10=PhotoImage(file='ee-PhotoRoom.png').subsample(2)
        image_label10=Label(n,image=arrow10,width=0,border=0,bg="#263997")
        image_label10.place(x=1050,y=220)
        arrow11=PhotoImage(file='images-PhotoRoom1.png').subsample(2)
        image_label11=Label(n,image=arrow11,width=0,border=0,bg="#263997")
        image_label11.place(x=950,y=450)
        arrow12=PhotoImage(file='33-PhotoRoom.png').subsample(2)
        image_label12=Label(n,image=arrow12,width=0,border=0,bg="#263997")
        image_label12.place(x=1070,y=450)
        def cal():
             subprocess.Popen(["python","calc.py"])
        def code():
           subprocess.Popen(["notepad.exe","calculator.txt"])
        def age():
             subprocess.Popen(["python","GUI Age Calculator.py"])
        def code1():
             subprocess.Popen(["notepad.exe","age.txt"])
        def xo():
             subprocess.Popen(["python","xo.py"])
        def code2():
             subprocess.Popen(["notepad.exe","xo.txt"])
        def roll():
             subprocess.Popen(["python","roll.py"])
        def code3():
             subprocess.Popen(["notepad.exe","roll.txt"])
        def tk():
             subprocess.Popen(["python","texttospeech.py"])
        def code4():
             subprocess.Popen(["notepad.exe","text.txt"])
        def pp():
             subprocess.Popen(["python","password.py"])
        def code5():
             subprocess.Popen(["notepad.exe","password.txt"])
        button4=Button(n,text="GUI Calculator ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=cal).place(x=10,y=10)
        button5=Button(n,text="Calculator Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=code).place(x=10,y=75)
        button6=Button(n,text="GUI Age Calculator ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=age).place(x=10,y=200)
        button6=Button(n,text="GUI Age Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=code1).place(x=10,y=270)
        button7=Button(n,text="Tic Tac toe ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=xo).place(x=10,y=420)
        button7=Button(n,text="XO Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackgroun="#641E16",command=code2).place(x=10,y=490)
        button8=Button(n,text="Dice Roller ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=roll).place(x=700,y=10)
        button8=Button(n,text="Dice Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackgroun="#641E16",command=code3).place(x=700,y=75)
        button9=Button(n,text="Text to speech ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=tk).place(x=700,y=200)
        button9=Button(n,text=" Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackgroun="#641E16",command=code4).place(x=700,y=270)
        button10=Button(n,text="Password Create",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=pp).place(x=700,y=420)
        button10=Button(n,text=" Code ",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackgroun="#641E16",command=code5).place(x=700,y=490)
        n.mainloop()
    def fourth():
         subprocess.Popen(["notepad.exe","lecture4.txt"])
    def fifth():
         subprocess.Popen(["notepad.exe","lecture5.txt"])
    button1=Button(py,text="Lecture 1",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=first).place(x=50,y=10)
    button2=Button(py,text="Lecture 2",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=second).place(x=750,y=90)
    button3=Button(py,text="Lecture 3",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=third).place(x=50,y=170)
    button4=Button(py,text="Tkinter",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=fou).place(x=410,y=450)
    button5=Button(py,text="Lecture 4",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=fourth).place(x=750,y=250)
    button6=Button(py,text="Lecture 5",font="Romes 20",fg="#52BE80",cursor="hand2",bd=5,activebackground="#641E16",command=fifth).place(x=50,y=330)

    py.mainloop()
button1=Button(window,text="Python",font="Romes 30",borderwidth=5,background="#A6ACAF",cursor="hand2",bd=5,activebackground="#641E16",command=py).place(x=150,y=300)
window.mainloop()
