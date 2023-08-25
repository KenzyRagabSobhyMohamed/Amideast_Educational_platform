from cProfile import label
from email.mime import image
from optparse import Values
from tkinter import *
import tkinter as tk
from datetime import date
import random
from pytube import YouTube
import pytube
from tkinter import messagebox
from tkinter.ttk import Combobox
from turtle import width
import pyttsx3
from PIL import Image,ImageTk
import os
roll=Tk()
roll.title("dice player")
roll.geometry("600x600")
roll.resizable(0,0)
roll.configure(bg="gray")
ll=Label(roll,text='',font=("Arial",250))

def roll1():    
        num=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        ll.config(text=f'{random.choice(num)}{random.choice(num)}')
        ll.pack()
button=Button(roll,text="click to play",borderwidth=2,fg="blue",bg="white",command=roll1,relief=SUNKEN) 
button.place(x=150,y=150)
button.pack()
roll.mainloop()
