from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter.ttk import Combobox
import pyttsx3


################### Initialized window####################

root = Tk()
root.geometry('500x300')
root.resizable(10,10)
root.config(bg = '#FFE873')
root.title('TECHARGE - TEXT TO SPEECH')
Label(root, text = 'TEXT TO SPEECH' , font='Verdana 30 bold' , bg ='#FFE873').place(x=30,y=10)
Label(root, text ='Enter Text', font ='Verdana 15 bold', bg ='#FFE873').place(x=30,y=70)
Msg = StringVar()
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=30 , y=120)
gender_combobox=Combobox(root,font="Arial",values=['male','female'])
gender_combobox.place(x=50,y=250)
speed_combo=Combobox(root,font="Arial",values=['normal','fast','slow'])
speed_combo.place(x=50,y=200)
gender_combobox.set('male')
speed_combo.set('normal')
engine=pyttsx3.init()
def speak():
         text=entry_field.get()
         gender=gender_combobox.get()
         speed=speed_combo.get()
         voices=engine.getProperty('voices')
         def setv():
            if gender=='male':
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
                engine.setProperty('voice',voices[1].id)
                engine.say(text)
                engine.runAndWait()
         if speed=="fast":
                 engine.setProperty('rate',250)
                 setv()
         elif speed=="normal":
                engine.setProperty('rate',150)
                setv()
         else:
                engine.setProperty('rate',80)
                setv()
    
def Exit():
    root.destroy() 
def Reset():
    Msg.set("")

Button(root, text = "PLAY" , font = 'Verdana 15 bold', command = speak, width =4).place(x=30, y=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=150)
Button(root, text = 'RESET', font='Verdana 15 bold', command = Reset).place(x=185 , y =150)
root.mainloop()
