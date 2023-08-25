from msilib.schema import ComboBox
from tkinter import*
from tkinter import messagebox
import random
from random import randint
from tkinter import ttk
import googletrans
from googletrans import Translator
import os
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
from tkinter.filedialog import Open
import webbrowser
import subprocess
from PIL import ImageTk,Image
import pyaudio
import wave
import speech_recognition as sr
import customtkinter
import textblob
from textblob import TextBlob
import threading

from cProfile import label
from cgitb import text
from fnmatch import translate
from operator import index
from optparse import Values
from sqlite3 import Cursor
from tkinter.tix import TEXT
from itertools import filterfalse


First=Tk()
First.geometry("1039x587+150+50")
First.resizable(False,False)
First.iconbitmap("photos\\neural.ico")
First.title("My graduation project")
F1=PhotoImage(file="photos\\first.png")
F11=Label(First,image=F1,borderwidth=0,highlightthickness=0,bd=0)
F11.pack()
SI=PhotoImage(file="photos\\homefinal3.png")
BI=PhotoImage(file="photos\\homefinal2.png")
l=PhotoImage(file="photos\\llll.png")
s=PhotoImage(file="photos\\s.png")
a=PhotoImage(file="photos\\A.png")
h=PhotoImage(file="photos\\H.png")


def HomeSignLog():
    global root
    global L
    global S
    global A
    global H
    global bi
    root=Toplevel(First)
    root.geometry("1039x587+150+50")
    root.resizable(False,False)
    root.iconbitmap("photos\\neural.ico")
    root.title("My graduation project")
    
    bi=Label(root,image=BI)
    bi.pack()
    
    L=Button(root,image=l,borderwidth=0,highlightthickness=0,bd=0,command=signin,activebackground="#041D3B")
    L.place(x=728,y=0)
    
    S=Button(root,image=s,borderwidth=0,highlightthickness=0,command=signup,activebackground="#041D3B")
    S.place(x=885,y=0)
    
    A=Button(root,image=a,borderwidth=0,command=about,highlightthickness=0,activebackground="#041D3B")
    A.place(x=570,y=0)
    
    H=Button(root,image=h,borderwidth=0,highlightthickness=0,command=home,activebackground="#041D3B")
    H.place(x=408,y=0)

    L.bind("<Enter>",loginH)
    L.bind("<Leave>",loginN)
    S.bind("<Enter>",signupH)
    S.bind("<Leave>",signupN)
    A.bind("<Enter>",AboutH)
    A.bind("<Leave>",AboutN)
    H.bind("<Enter>",homeH)
    H.bind("<Leave>",homeN)


con=PhotoImage(file="photos\\continue.png")
C=Button(First,image=con,command=HomeSignLog,borderwidth=0,highlightthickness=0,bd=0,activebackground="#03010F")
C.place(x=15,y=400)
arrowR=PhotoImage(file="photos\\arrowR.png")
AR=Label(First,image=arrowR,borderwidth=0,highlightthickness=0,bd=0,activebackground="#03010F")
AR.place(x=20,y=455)
def ContE(e):
    AR.place(x=110,y=455)
def ContL(l):
    AR.place(x=20,y=455)
C.bind("<Enter>",ContE)
C.bind("<Leave>",ContL)





um=PhotoImage(file="photos\\usermain3.png")
SDGsW=PhotoImage(file="photos\\SDGsW.png")
sada=PhotoImage(file="photos\\sada.png")
story_image=PhotoImage(file="photos\\storywindow.png")



global signupF
global signinF
global aboutF

signupF=Frame()
signinF=Frame()
aboutF=Label()



#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
global user
global password
global confirm
global userL
global passwordL
global currentuser
global engine 
engine = pyttsx3.init()


#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################




#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################






#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################















arrowright=PhotoImage(file="photos\\arrowright.png")   
arrowleft=PhotoImage(file="photos\\arrowleft.png")   
listen=PhotoImage(file="photos\\listenfinal2.png")   
voice=PhotoImage(file="photos\\voicefinal.png")
speed=PhotoImage(file="photos\\speedfinal.png")   


ProgrammingP=PhotoImage(file="photos\\learnProgramming.png")
environmentP=PhotoImage(file="photos\\environmentP.png")
EnglishP=PhotoImage(file="photos\\EnglishP.png")
embeddedP=PhotoImage(file="photos\\embeddedP.png")

#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
global Assistantgender
global Voices
Assistantgender="Female"
Voices=engine.getProperty('voices')





def SpeechR():
    
    # Set parameters for recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3
    

    # Initialize PyAudio object and open stream for recording
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Record audio for specified duration
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save recorded audio to a WAV file
    wf = wave.open("recorded_audio.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

    # Load recorded audio file and initialize recognizer object
    r = sr.Recognizer()
    with sr.AudioFile("recorded_audio.wav") as source:
        audio_data = r.record(source)

    # Convert speech to text using Google Speech Recognition API
    try:
        text = r.recognize_google(audio_data)
        print(f"Speech recognized: {text}")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    english_keywords     = ["english", "language"      ,"speaking"   ,"listening","writing"]
    programming_keywords = ["code"   , "programming"   , "python"    , "program"]
    sdg_keywords         = ["goals"  , "sustainability","development","green"]
    
    for english_key in english_keywords:
        if english_key in text.lower():
            if (Assistantgender=="Female"):
                engine.setProperty('voice', Voices[1].id)
            else:
                engine.setProperty('voice', Voices[0].id)
            engine.say("I'm happy that you want to learn English. Now, I will take you to the English section")
            engine.runAndWait()
            EnglishW()
            return

    for programming_key in programming_keywords:
        if programming_key in text.lower():
            if (Assistantgender=="Female"):
                engine.setProperty('voice', Voices[1].id)
            else:
                engine.setProperty('voice', Voices[0].id)
            engine.say("I'm happy that you want to learn Programming. Now, I will take you to the programming section")
            engine.runAndWait()
            py()
            return

    for sdg_key in sdg_keywords:
        if sdg_key in text.lower():
            if (Assistantgender=="Female"):
                engine.setProperty('voice', Voices[1].id)
            else:
                engine.setProperty('voice', Voices[0].id)
            engine.say("I'm happy that you want to learn SDGs. Now, I will take you to the sustainability section")
            engine.runAndWait()
            SustainabilityW()
            return







#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
    
def Usermain():
    global usermain
    usermain=Toplevel(root)
    usermain.geometry("1039x587+150+50")
    usermain.resizable(False,False)
    usermain.iconbitmap("photos\\neural.ico")
    usermain.title("My graduation project")
    
    UM=Label(usermain,image=um)
    UM.pack()


    L1=Label(usermain,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    BME=Button(usermain,text="Learn English",bg="#010220",width=20,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=EnglishW,activebackground="#010220")
    BME.place(x=395,y=500)
    BMP=Button(usermain,text="Learn Programming",bg="#010220",width=20,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=py,activebackground="#010220")
    BMP.place(x=65,y=290)
    BMP1=Button(usermain,text="Learn about sustainability",bg="#010220",width=20,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=SustainabilityW,activebackground="#010220")
    BMP1.place(x=400,y=290)
    BMP=Button(usermain,text="Learn about embedded\n   systems",bg="#010220",width=20,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=com,activebackground="#010220")
    BMP.place(x=740,y=290)
    buttonA=Button(usermain,text="Speak to\nmy assistant",bg="#021B3E",width=20,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=SpeechR,activebackground="#010220")
    buttonA.place(x=300,y=20)

    #PP=Label(usermain,image=ProgrammingP,borderwidth=0,highlightthickness=0,bd=0,activebackground="#041D3B")
    #PP.place(x=728,y=0)
    #Bm1=Button(usermain,text="Story generator", command = StorygeneratorW)
    #Bm1.place(x=200,y=100)
################################################################################
benglish1=PhotoImage(file="photos\\benglish1.png")
benglish2=PhotoImage(file="photos\\benglish22.png")
benglish3=PhotoImage(file="photos\\benglish3.png")
testL=PhotoImage(file="photos\\testL.png")
Trans=PhotoImage(file="photos\\Trans.png")
Flash=PhotoImage(file="photos\\Flash.png")
SpeakingL=PhotoImage(file="photos\\SpeakingL.png")
photosR=PhotoImage(file="photos\\photosE.png")
photosR2=PhotoImage(file="photos\\pppppp2.png")

def EnglishW():
    EnglishW=Toplevel(usermain)
    EnglishW.geometry("1039x587+150+50")
    EnglishW.resizable(False,False)
    EnglishW.iconbitmap("photos\\neural.ico")
    EnglishW.title("My graduation project")
    UM=Label(EnglishW,image=sada)
    UM.pack()
    L1=Label(EnglishW,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    BMP=Button(EnglishW,image=benglish1,bd=0,highlightthickness=0,fg="white",command=StorygeneratorW)
    BMP.place(x=170,y=154)
    BMP=Button(EnglishW,image=benglish2,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=checker_page)
    BMP.place(x=170,y=275)
    BMP=Button(EnglishW,image=Trans,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=transalet)
    BMP.place(x=170,y=390)
    BMP=Button(EnglishW,image=testL,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=lisinng)
    BMP.place(x=700,y=154)
    BMP=Button(EnglishW,image=Flash,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=embeddedW)
    BMP.place(x=700,y=275)
    BMP=Button(EnglishW,image=SpeakingL,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white",command=speaking_practise)
    BMP.place(x=700,y=390)
    ff=Label(EnglishW,image=photosR,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white")
    ff.place(x=40,y=130)
    ff=Label(EnglishW,image=photosR2,bd=0,font=("tajawal",14,"bold"),highlightthickness=0,fg="white")
    ff.place(x=600,y=140)



#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#####################Listening###########################


def lisinng():
 global hinter,hint_count,answer_label,my_entry,hint_label,words,count

 listiing = Toplevel()
 listiing.title("Listening Practise")
 listiing.geometry("550x410")
 listiing.config(bg="#00a1e4")

 words = [
    "Hello",
    "Goodbye",
    "Please",
    "Thank you",
    "Sorry",
    "Yes",
    "No",
    "Who",
    "Dictionary",
    "Car",
    "Cat",
    "Programming",
    "Python",
    "Translate",
    "Book",
    "Lock",
    "Door",
    "Window",
    "Apple",
    "Row",
    "NoteBook",
    "Pending",
    "Library",
    "Science",
    "England",
    "USA",
    "Embassy",
    "Region",
    "Why",
    "Where"
]

 count = len(words)
 hinter = ""
 hint_count = 0


 answer_label = Label(listiing, text="",bg="#00a1e4")
 answer_label.pack(pady=20)

 my_entry = Entry(listiing, font=("Helvetica", 18))
 my_entry.pack(pady=20)

 button_frame = Frame(listiing,bg="#00a1e4")
 button_frame.pack(pady=20)

 answer_button = customtkinter.CTkButton(button_frame, text="Answer", command=answer2,hover_color="#e3b115",fg_color="#fec20b",text_color="black")
 answer_button.grid(row=0, column=0, padx=20)

 next_button = customtkinter.CTkButton(button_frame, text="Next", command=next2,hover_color="#e3b115",fg_color="#fec20b",text_color="black")
 next_button.grid(row=0, column=1,)

 hint_button = customtkinter.CTkButton(button_frame, text="Hint", command=hint2,hover_color="#e3b115",fg_color="#fec20b",text_color="black")
 hint_button.grid(row=0, column=2, padx=20)
 mutton=customtkinter.CTkButton(button_frame,text="Click To Hear!",hover_color="#e3b115",fg_color="#fec20b",text_color="black",command=saying)
 mutton.grid(row=1, column=1, pady=20)

 hint_label = Label(listiing, text="",bg="#00a1e4")
 hint_label.pack(pady=20)

 next2()

def next2():
    global hinter,hint_count,answer_label,my_entry,hint_label,words,count
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0, count-1)

def answer2():
    global hint_count
    global hinter
    if my_entry.get().capitalize() == words[random_word]:
        answer_label.config(text=f"Correct!")
    else:

        answer_label.config(text=f"Incorrect! is not {my_entry.get().capitalize()} Try again!") 
        if hint_count < len(words[random_word]):
         hinter = hinter + words[random_word][hint_count]
         hint_label.config(text=hinter)
         hint_count +=1

def hint2():
    global hint_count
    global hinter

    if hint_count < len(words[random_word]):
        hinter = hinter + words[random_word][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1

def saying():
    way = pyttsx3.init()
    wordy = f"{words[random_word]}"
    way.say(wordy)
    way.runAndWait()







def checker_page():
 global customer_word,spell_label,checker
 checker= Toplevel()
 checker.title("Spelling Checker",)
 checker.config(bg="#00a1e4")
 checker.geometry("700x400")
 Label(checker,text="Spelling Checker",bg="#00a1e4" ,font=("Helvetica", 36)).pack(pady=50)
 customer_word =StringVar()
 Entry(checker,textvariable=customer_word,justify="center", font=("Helvetica", 36)).pack(pady=20)
 customtkinter.CTkButton(checker,text="check",command=check_spelling,hover_color="#e3b115",fg_color="#fec20b",text_color="black").pack()
 spell_label = Label(checker,text="",bg="#00a1e4", font=("Helvetica", 20))
 spell_label.place(x=350,y=350)

def check_spelling():
    global customer_word,spell_label,checker
    word_check = customer_word.get()
    checked=TextBlob(word_check)
    text_checked =str(checked.correct())

    cs = Label(checker, text="Correct Spelling is :",
               bg="#00a1e4", font=("Helvetica", 20))
    cs.place(x=100,y=350)
    spell_label.config(text=text_checked)








def transalet():
 global t,t2,como,como1
 k=Toplevel()
 k.title("Amideast Translate")
 k.geometry("1039x587+150+50")
 k.config(bg="#00a1e4")
 como=ttk.Combobox(k,values=landv,font="Roboto 15",state="r")
 como.place(x=110,y=50)
 como.set("english")
 f2=Frame(k,bg="#263997",bd=5)
 f2.place(x=530,y=100,width=440,height=210)
 t2=Text(f2,font="Romes 15",bg="WHITE",relief=GROOVE,wrap=WORD)
 t2.place(x=0,y=0,width=420,height=200)
 scrol=Scrollbar(f2)
 scrol.pack(side="right",fill="y")
 como1=ttk.Combobox(k,values=landv,font="Roboto 15",state="r")
 como1.place(x=630,y=50)
 como1.set("arabic")
 f=Frame(k,bg="#263997",bd=5)
 f.place(x=10,y=100,width=440,height=210)
 t=Text(f,font="Romes 15",bg="WHITE",relief=GROOVE,wrap=WORD)
 t.place(x=0,y=0,width=420,height=200)
 scrol=Scrollbar(f)
 scrol.pack(side="right",fill="y")
 b1=customtkinter.CTkButton(k,text="Translate",cursor="hand2",command=translate_now,hover_color="#e3b115",fg_color="#fec20b",text_color="black")
 b1.place(x=10,y=330)
 b2=customtkinter.CTkButton(k,text="Clear",cursor="hand2",command=clear,hover_color="#e3b115",fg_color="#fec20b",text_color="black") 
 b2.place(x=890,y=330)
 b2=customtkinter.CTkButton(k,text="Exit",cursor="hand2",command=k.destroy,hover_color="#e3b115",fg_color="#fec20b",text_color="black")
 b2.place(x=890,y=390)
 

lang=googletrans.LANGUAGES
landv=list(lang.values())
langu=lang.keys()

def clear():
    global t,t2

    t.delete(1.0,END)
    t2.delete(1.0,END)

def translate_now():
       global t,t2,como,como1

       t2.delete(1.0,END)
       for key,value in lang.items():
           if value == como.get():
               k1=key
       for key,value in lang.items():
           if value == como1.get():
               k2=key
       words=textblob.TextBlob(t.get("1.0",END))
       words=words.translate(from_lang=k1, to=k2)
       t2.insert(1.0,words)





def speaking_practise():
    speaking_window = Toplevel(usermain)
    speaking_window.title("Speaking Practise")
    speaking_window.geometry("500x500")
    speaking_window.resizable(False, False)
    speaking_window.config(bg="#00a1e4")

    Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
    character = [' there lived a king.', ' there was a man named Jack.', ' there lived a farmer.']
    time = [' One day', ' One full-moon night']
    story_plot = [' he was passing by', ' he was going for a picnic to ']
    place = [' the mountains', ' the garden']
    second_character = [' he saw a man', ' he saw a young lady']
    age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
    work = [' searching something.', ' digging a well on roadside.']

    story = f"{random.choice(Sentence_starter)}  {random.choice(character)} \n {random.choice(time)} {random.choice(story_plot)} \n  {random.choice(place)} {random.choice(second_character)} \n {random.choice(age) + random.choice(work)}"
    story_label = Label(speaking_window, text=story, bg="#00a1e4", fg="white", font=("Helvtica", 12)).place(x=48, y=50)
    r= sr.Recognizer()
    def speech_to_text():

        # global time_label
        # time_label = Label(speaking_window, text=" ", bg="#00a1e4", fg="white", font=("Helvtica", 12)).place(x=48,y=170)
        # def clock():
        #    time_label.config(text= str(15-counter))
        #    time_label.after(1000, clock)

        with sr.Microphone() as source:
            # read the audio data from the default microphone
            # clock()
            audio_data = r.record(source, duration=8)
            # convert speech to text
            text = r.recognize_google(audio_data)
            text_list = list(text.split(" "))
            ii = 0
            while (ii < len(text_list)):
                text_list.insert(ii, "\n")
                ii += 7
            text = ' '.join(text_list)
        text_label = Label(speaking_window, text=text, bg="#00a1e4", fg="white", font=("Helvtica", 12)) #.place(x=48,y=250)
        story_list = list(story.split(" "))
        jj = 0
        counter = 0
        while (jj < len(text_list)):
            if text_list[jj] in story_list:
                counter += 1
            jj += 1
        score = int((counter / len(text_list)) * 100)
        if score<75:
            score+=20
        else:
            score=97



        score_text = f"You scored {score}/100"
        score_label = Label(speaking_window, text=score_text, bg="#00a1e4", fg="white", font=("Helvtica", 12)).place(
            x=48, y=350)

    speaking_button = customtkinter.CTkButton(speaking_window, height=20, fg_color="#fec20b", text="Speak",
                                              text_color="black", cursor="hand2", hover_color="#e3b115",
                                              command=threading.Thread(target=speech_to_text).start).place(x=175, y=200)

#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################


New=PhotoImage(file='photos\\New.png')
imag=PhotoImage(file='photos\\pythonBack.png')
TkinterB=PhotoImage(file='photos\\TkinterBB.png')
lec1=PhotoImage(file='photos\\lec11.png')
lec2=PhotoImage(file='photos\\lec22.png')
lec3=PhotoImage(file='photos\\lec33.png')
lec4=PhotoImage(file='photos\\lec44.png')
lec5=PhotoImage(file='photos\\lec55.png')
back=PhotoImage(file='photos\\New.png')
calculatorP=PhotoImage(file='photos\\calculator.png')
AcalculatorP=PhotoImage(file='photos\\age-calculator.png')
tic=PhotoImage(file='photos\\tic.png')
dic=PhotoImage(file='photos\\dic.png')
T2S=PhotoImage(file='photos\\T2S.png')
pas=PhotoImage(file='photos\\pas.png')

def py():
    py=Toplevel(usermain)
    py.geometry("1039x587+150+50")
    py.resizable(False,False)
    icon=PhotoImage(file='photoskoky\\mm.png')
    py.iconphoto(False,icon)
    py.title("learning python")
    l1=Label(py,image=imag)
    l1.pack()
    L1=Label(py,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    #Label(py,text="in this lecture you will learn how to apply the print functions in python and its items",font="Arial 12").place(x=10,y=80)
    #Label(py,text="in this lecture you will learn how to apply the print functions in python and its items",font="Arial 12").place(x=10,y=120)
    def first():
        subprocess.Popen(["notepad.exe","photoskoky\\lecture1.txt"])
    def second():
        subprocess.Popen(["notepad.exe","photoskoky\\lecture2.txt"])
    def third():
        subprocess.Popen(["notepad.exe","photoskoky\\lecture3.txt"])
    def fou():
        n=Toplevel(py)
        n.title("Tkinter")
        n.geometry("1039x587+150+50")
        n.resizable(False,False)
        pl=Label(n,image=sada)
        pl.pack()
        L1l=Label(n,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
        L1l.place(x=140,y=30)
        #arrow1=PhotoImage(file='photos\\calculator.png').subsample(3)
        image_label1=Label(n,image=calculatorP,border=0,bg="#010220")
        image_label1.place(x=260,y=140)
        #arrow2=PhotoImage(file='photoskoky\\images-PhotoRoom1.png').subsample(2)
        image_label2=Label(n,image=AcalculatorP,border=0,bg="#010220")
        image_label2.place(x=260,y=290)
        #arrow3=PhotoImage(file='photoskoky\\images-PhotoRoom1.png').subsample(2)
        image_label3=Label(n,image=tic,border=0,bg="#010220")
        image_label3.place(x=550,y=140)
        #arrow4=PhotoImage(file='photoskoky\\2941875-200-PhotoRoom.png').subsample(2)
        image_label4=Label(n,image=dic,border=0,bg="#010220")
        image_label4.place(x=550,y=290)
        #arrow5=PhotoImage(file='photoskoky\\images-PhotoRoom1.png').subsample(2)
        image_label5=Label(n,image=T2S,border=0,bg="#010220")
        image_label5.place(x=890,y=140)
        #arrow6=PhotoImage(file='photoskoky\\ss-PhotoRoom.png').subsample(2)
        image_label6=Label(n,image=pas,border=0,bg="#263997")
        image_label6.place(x=890,y=290)

        def cal():
             subprocess.Popen(["python","photoskoky\\calc.py"])
        def code():
           subprocess.Popen(["notepad.exe","photoskoky\\calculator.txt"])
        def age():
             subprocess.Popen(["python","photoskoky\\GUI Age Calculator.py"])
        def code1():
             subprocess.Popen(["notepad.exe","photoskoky\\age.txt"])
        def xo():
             subprocess.Popen(["python","photoskoky\\xo.py"])
        def code2():
             subprocess.Popen(["notepad.exe","photoskoky\\xo.txt"])
        def roll():
             subprocess.Popen(["python","photoskoky\\roll.py"])
        def code3():
             subprocess.Popen(["notepad.exe","photoskoky\\roll.txt"])
        def tk():
             subprocess.Popen(["python","photoskoky\\T2S.py"])
        def code4():
             subprocess.Popen(["notepad.exe","photoskoky\\text.txt"])
        def pp():
             subprocess.Popen(["python","photoskoky\\password.py"])
        def code5():
             subprocess.Popen(["notepad.exe","photoskoky\\password.txt"])

        button4=Button(n,text="GUI Calculator ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=cal,bg="#010220").place(x=10,y=150)
        button5=Button(n,text="Calculator Code ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=code,bg="#010220").place(x=10,y=200)
        button6=Button(n,text="GUI Age Calculator ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=age,bg="#010220").place(x=10,y=300)
        button6=Button(n,text="GUI Age Code ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=code1,bg="#010220").place(x=10,y=350)
        button7=Button(n,text="Tic Tac toe ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=xo,bg="#010220").place(x=400,y=150)
        button7=Button(n,text="XO Code ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackgroun="#010220",command=code2,bg="#010220").place(x=400,y=200)
        button8=Button(n,text="Dice Roller ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=roll,bg="#010220").place(x=400,y=300)
        button8=Button(n,text="Dice Code ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackgroun="#010220",command=code3,bg="#010220").place(x=400,y=350)
        button9=Button(n,text="Text to speech ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=tk,bg="#010220").place(x=680,y=150)
        button9=Button(n,text=" Code ",font=("Romes",18,"bold"),fg="white",cursor="hand2",bd=0,activebackgroun="#010220",command=code4,bg="#010220").place(x=680,y=200)
        button10=Button(n,text="Get Password",font=("Romes",20,"bold"),fg="white",cursor="hand2",bd=0,activebackground="#010220",command=pp,bg="#010220").place(x=680,y=300)
        button10=Button(n,text=" Code ",font=("Romes",20,"bold"),fg="white",cursor="hand2",bd=0,activebackgroun="#010220",command=code5,bg="#010220").place(x=680,y=350)
        n.mainloop()
    def fourth():
         subprocess.Popen(["notepad.exe","photoskoky\\lecture4.txt"])
    def fifth():
         subprocess.Popen(["notepad.exe","photoskoky\\lecture5.txt"])
    button1=Button(py,image=lec1,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=first,highlightthickness=0).place(x=50,y=170)
    button2=Button(py,image=lec2,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=second,highlightthickness=0).place(x=50,y=270)
    button3=Button(py,image=lec3,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=third,highlightthickness=0).place(x=50,y=370)
    button4=Button(py,image=TkinterB,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=fou,highlightthickness=0).place(x=390,y=490)
    button5=Button(py,image=lec4,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=fourth,highlightthickness=0).place(x=750,y=205)
    button6=Button(py,image=lec5,font="Romes 20",fg="#52BE80",cursor="hand2",bd=0,activebackground="#641E16",command=fifth,highlightthickness=0).place(x=750,y=305)

    py.mainloop()





###############################################################

def com():
    com=Toplevel(usermain)
    com.title("Embedded System")
    com.geometry("1039x587+150+50")
    #com.config(bg="#010220")
    com.resizable(False,False)
    arrow6=PhotoImage(file='photos\\2.png').subsample(2)
    image_label6=Label(com,image=arrow6,width=0,border=0,bg="#263997")
    image_label6.place(x=30,y=30)
    arrow11=PhotoImage(file='photos\\11.png').subsample(2)
    image_label11=Label(com,image=arrow11,width=0,border=0,bg="#263997")
    image_label11.place(x=120,y=30)
    arrow12=PhotoImage(file='photos\\12.png').subsample(2)
    image_label12=Label(com,image=arrow12,width=0,border=0,bg="#263997")
    image_label12.place(x=630,y=30)
    arrow13=PhotoImage(file='photos\\13.png').subsample(2)
    image_label13=Label(com,image=arrow13,width=0,border=0,bg="#263997")
    image_label13.place(x=730,y=30)
    arrow10=PhotoImage(file='photos\\10.png').subsample(2)
    image_label10=Label(com,image=arrow10,width=0,border=0,bg="#263997")
    image_label10.place(x=830,y=35)
    Label(com,text="Components:",font="Arial 15 bold").place(x=20,y=0)
    arrow4=PhotoImage(file='photos\\3.png').subsample(2)
    image_label4=Label(com,image=arrow4,width=0,border=0,bg="#263997")
    image_label4.place(x=220,y=30)
    arrow5=PhotoImage(file='photos\\4.png').subsample(2)
    image_label5=Label(com,image=arrow5,width=0,border=0,bg="#263997")
    image_label5.place(x=320,y=30)
    arrow2=PhotoImage(file='photos\\6.png').subsample(2)
    image_label2=Label(com,image=arrow2,width=0,border=0,bg="#263997")
    image_label2.place(x=420,y=35)
    arrow7=PhotoImage(file='photos\\7.png').subsample(2)
    image_label7=Label(com,image=arrow7,width=0,border=0,bg="#263997")
    image_label7.place(x=520,y=30)
    arrow8=PhotoImage(file='photos\\8.png').subsample(2)
    image_label8=Label(com,image=arrow8,width=0,border=0,bg="#263997")
    image_label8.place(x=930,y=30)
    arrow9=PhotoImage(file='photos\\9.png').subsample(2)
    image_label9=Label(com,image=arrow9,width=0,border=0,bg="#263997")
    image_label9.place(x=35,y=195)
    arrow14=PhotoImage(file='photos\\14.png').subsample(2)
    image_label14=Label(com,image=arrow14,width=0,border=0,bg="#263997")
    image_label14.place(x=120,y=185)
    arrow15=PhotoImage(file='photos\\15.png').subsample(2)
    image_label15=Label(com,image=arrow15,width=0,border=0,bg="#263997")
    image_label15.place(x=220,y=185)
    arrow16=PhotoImage(file='photos\\16.png').subsample(2)
    image_label16=Label(com,image=arrow16,width=0,border=0,bg="#263997")
    image_label16.place(x=320,y=185)
    arrow17=PhotoImage(file='photos\\17.png').subsample(2)
    image_label17=Label(com,image=arrow17,width=0,border=0,bg="#263997")
    image_label17.place(x=420,y=185)
    arrow18=PhotoImage(file='photos\\18.png').subsample(2)
    image_label18=Label(com,image=arrow18,width=0,border=0,bg="#263997")
    image_label18.place(x=520,y=190)
    arrow19=PhotoImage(file='photos\\19.png').subsample(2)
    image_label19=Label(com,image=arrow19,width=0,border=0,bg="#263997")
    image_label19.place(x=620,y=190)
    arrow21=PhotoImage(file='photos\\21.png').subsample(2)
    image_label21=Label(com,image=arrow21,width=0,border=0,bg="#263997")
    image_label21.place(x=720,y=190)
    arrow22=PhotoImage(file='photos\\22.png').subsample(2)
    image_label22=Label(com,image=arrow22,width=0,border=0,bg="#263997")
    image_label22.place(x=820,y=185)
    arrow23=PhotoImage(file='photos\\23.png').subsample(2)
    image_label23=Label(com,image=arrow23,width=0,border=0,bg="#263997")
    image_label23.place(x=920,y=185)
    arrow24=PhotoImage(file='photos\\24.png').subsample(2)
    image_label24=Label(com,image=arrow24,width=0,border=0,bg="#263997")
    image_label24.place(x=30,y=340)
    arrow25=PhotoImage(file='photos\\25.png').subsample(2)
    image_label25=Label(com,image=arrow25,width=0,border=0,bg="#263997")
    image_label25.place(x=120,y=340)
    arrow26=PhotoImage(file='photos\\26.png').subsample(2)
    image_label26=Label(com,image=arrow26,width=0,border=0,bg="#263997")
    image_label26.place(x=220,y=360)
    arrow27=PhotoImage(file='photos\\27.png').subsample(2)
    image_label27=Label(com,image=arrow27,width=0,border=0,bg="#263997")
    image_label27.place(x=320,y=370)
    arrow28=PhotoImage(file='photos\\28.png').subsample(2)
    image_label28=Label(com,image=arrow28,width=0,border=0,bg="#263997")
    image_label28.place(x=420,y=370)
    arrow30=PhotoImage(file='photos\\30.png').subsample(2)
    image_label30=Label(com,image=arrow30,width=0,border=0,bg="#263997")
    image_label30.place(x=520,y=370)
    arrow29=PhotoImage(file='photos\\29.png').subsample(2)
    image_label29=Label(com,image=arrow29,width=0,border=0,bg="#263997")
    image_label29.place(x=620,y=370)
    def py():
        py=Toplevel(com)
        py.title("Circuits")
        py.geometry("1039x587+150+50")
        py.config(bg="#010220")
        py.resizable(False,False)
        def c1():
             webbrowser.open("https://www.tinkercad.com/things/32cz4CdpEcX-neat-kieran-kasi")
        def c2():
             webbrowser.open("https://www.tinkercad.com/things/8mWRNZ0Ct6R-fantastic-habbi")
        def c3():
             webbrowser.open("https://www.tinkercad.com/things/idFQU9aQ8gw-1")
        def c4():
             webbrowser.open("https://www.tinkercad.com/things/csuHZWXogUI")
        def c5():
             webbrowser.open("https://www.tinkercad.com/things/lpMDa2apYGv-daring-jaban-jofo")
        def c6():
             webbrowser.open("https://www.tinkercad.com/things/4ELeCt8yerK-copy-of-lcd-ultrasonic-sensor")
        def c7():
             webbrowser.open("https://www.tinkercad.com/things/bHLeA1olFpa-brave-kieran-blorr")
        def c8():
            webbrowser.open("https://www.tinkercad.com/things/5aXl77Bs2GT-flame-sensor")

        def c9():
            webbrowser.open("https://www.tinkercad.com/things/74ZNU8Mht1B-activity11-arduino-gas-sensor")
        arrow6=PhotoImage(file='photos\\l11.png').subsample(3)
        image_label6=Label(py,image=arrow6,width=0,border=0,bg="#263997")
        arrow7=PhotoImage(file='photos\\l22.png').subsample(3)
        image_label7=Label(py,image=arrow7,width=0,border=0,bg="#263997")
        arrow8=PhotoImage(file='photos\\l3.png').subsample(3)
        image_label8=Label(py,image=arrow8,width=0,border=0,bg="#263997")
        arrow9=PhotoImage(file='photos\\1.png').subsample(3)
        image_label9=Label(py,image=arrow9,width=0,border=0,bg="#263997")
        arrow1=PhotoImage(file='photos\\l5.png').subsample(3)
        image_label1=Label(py,image=arrow1,width=0,border=0,bg="#263997")
        arrow2=PhotoImage(file='photos\\h11.png').subsample(3)
        image_label2=Label(py,image=arrow2,width=0,border=0,bg="#263997")
        arro1=PhotoImage(file='photos\\f1.png').subsample(3)
        image_la=Label(py,image=arro1,width=0,border=0,bg="#263997")
        ar = PhotoImage(file='photos\\x1.png').subsample(4)
        image_la = Label(py, image=ar, width=0, border=0, bg="#263997")
        ar1 = PhotoImage(file='photos\\lk.png').subsample(5)
        image_la = Label(py, image=ar1, width=0, border=0, bg="#263997")
        button4=Button(py,image=arrow6,cursor="hand2",bd=8,activebackground="#641E16",command=c1).place(x=10,y=10)
        button5=Button(py,image=arrow7,cursor="hand2",bd=8,activebackground="#641E16",command=c2).place(x=350,y=10)
        button6=Button(py,image=arrow8,cursor="hand2",bd=8,activebackground="#641E16",command=c3).place(x=700,y=10)
        button7=Button(py,image=arrow9,cursor="hand2",bd=8,activebackground="#641E16",command=c5).place(x=10,y=200)
        button8=Button(py,image=arrow1,cursor="hand2",bd=8,activebackground="#641E16",command=c4).place(x=350,y=200)
        button9=Button(py,image=arrow2,cursor="hand2",bd=8,activebackgroun="#641E16",command=c6).place(x=700,y=200)
        button10=Button(py,image=arro1,cursor="hand2",bd=8,activebackground="#641E16",command=c7).place(x=350,y=400)
        button10=Button(py,image=ar,cursor="hand2",bd=8,activebackground="#641E16",command=c8).place(x=10,y=400)
        button10=Button(py,image=ar1,cursor="hand2",bd=8,activebackground="#641E16",command=c9).place(x=700,y=380)

        py.mainloop()
    button2=Button(com,text="Embedded System",font="Romes 12",borderwidth=5,background="#A6ACAF",cursor="hand2",bd=5,activebackground="#641E16",command=py).place(x=800,y=390)
    com.mainloop()


#################################################################

Goal1=PhotoImage(file="photos\\sustainable.png")
what=PhotoImage(file="photos\\what are sdgs.png")
textL=PhotoImage(file="photos\\textL.png")


def SustainabilityW():
    global SustainabilityW
    SustainabilityW=Toplevel(usermain)
    SustainabilityW.geometry("1039x587+150+50")
    SustainabilityW.resizable(False,False)
    SustainabilityW.iconbitmap("photos\\neural.ico")
    SustainabilityW.title("My graduation project")
    UM=Label(SustainabilityW,image=sada)
    UM.pack()
    L1=Label(SustainabilityW,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    G1=Button(SustainabilityW,image=Goal1,bg="#010220",bd=0,activebackground="#010220",command=Goals)
    G1.place(x=400,y=120)
    def ShowL():
        LabelW=Label(SustainabilityW,image=textL,bg="#010220",bd=0,activebackground="#010220")
        LabelW.place(x=50,y=200)
    What=Button(SustainabilityW,image=what,bg="#010220",bd=0,activebackground="#010220",command=ShowL)
    What.place(x=50,y=140)


    



g1=PhotoImage(file="photos\\SDGs\\g1.png")
g2=PhotoImage(file="photos\\SDGs\\g2.png")
g3=PhotoImage(file="photos\\SDGs\\g3.png")
g4=PhotoImage(file="photos\\SDGs\\g4.png")
g5=PhotoImage(file="photos\\SDGs\\g5.png")
g6=PhotoImage(file="photos\\SDGs\\g6.png")
g7=PhotoImage(file="photos\\SDGs\\g7.png")
g8=PhotoImage(file="photos\\SDGs\\g8.png")
g9=PhotoImage(file="photos\\SDGs\\g9.png")
g10=PhotoImage(file="photos\\SDGs\\g10.png")
g11=PhotoImage(file="photos\\SDGs\\g11.png")
g12=PhotoImage(file="photos\\SDGs\\g12.png")
g13=PhotoImage(file="photos\\SDGs\\g13.png")
g14=PhotoImage(file="photos\\SDGs\\g13.png")
g13=PhotoImage(file="photos\\SDGs\\g14.png")
g15=PhotoImage(file="photos\\SDGs\\g15.png")
g16=PhotoImage(file="photos\\SDGs\\g16.png")
g17=PhotoImage(file="photos\\SDGs\\g17.png")
Line=PhotoImage(file="photos\\line.png")
SDGss=PhotoImage(file="photos\\sdgss.png")

linkGoal1="https://www.un.org/sustainabledevelopment/poverty/"
linkGoal2="https://www.un.org/sustainabledevelopment/hunger/"
linkGoal3="https://www.un.org/sustainabledevelopment/health/"
linkGoal4="https://www.un.org/sustainabledevelopment/education/"
linkGoal5="https://www.un.org/sustainabledevelopment/gender-equality/"
linkGoal6="https://www.un.org/sustainabledevelopment/water-and-sanitation/"
linkGoal7="https://www.un.org/sustainabledevelopment/energy/"
linkGoal8="https://www.un.org/sustainabledevelopment/economic-growth/"
linkGoal9="https://www.un.org/sustainabledevelopment/infrastructure-industrialization/"
linkGoal10="https://www.un.org/sustainabledevelopment/inequality/"
linkGoal11="https://www.un.org/sustainabledevelopment/cities/"
linkGoal12="https://www.un.org/sustainabledevelopment/sustainable-consumption-production/"
linkGoal13="https://www.un.org/sustainabledevelopment/oceans/"
linkGoal14="https://www.un.org/sustainabledevelopment/climate-change/"
linkGoal15="https://www.un.org/sustainabledevelopment/biodiversity/"
linkGoal16="https://www.un.org/sustainabledevelopment/peace-justice/"
linkGoal17="https://www.un.org/sustainabledevelopment/globalpartnerships/"








def Goals():
    Goals=Toplevel(SustainabilityW)
    Goals.geometry("1039x587+150+50")
    Goals.resizable(False,False)
    Goals.iconbitmap("photos\\neural.ico")
    Goals.title("My graduation project")
    UM=Label(Goals,image=sada)
    UM.pack()
    L1=Label(Goals,text=currentuser,fg="white",bg="#021B3E",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    line=Button(Goals,image=Line,bg="#010220",bd=0,activebackground="#010220",command=Goals)
    line.place(x=0,y=130)

    G1=Button(Goals,image=g1,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal1)
    G1.place(x=30,y=150)
    G2=Button(Goals,image=g2,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal2)
    G2.place(x=130,y=150)
    G3=Button(Goals,image=g3,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal3)
    G3.place(x=230,y=150)
    G4=Button(Goals,image=g4,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal4)
    G4.place(x=330,y=150)
    G5=Button(Goals,image=g5,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal5)
    G5.place(x=430,y=150)
    G6=Button(Goals,image=g6,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal6)
    G6.place(x=530,y=150)
    G7=Button(Goals,image=g7,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal7)
    G7.place(x=630,y=150)
    G8=Button(Goals,image=g8,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal8)
    G8.place(x=730,y=150)
    G9=Button(Goals,image=g9,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal9)
    G9.place(x=830,y=150)
    G10=Button(Goals,image=g10,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal10)
    G10.place(x=930,y=150)
    G11=Button(Goals,image=g11,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal11)
    G11.place(x=30,y=300)
    G12=Button(Goals,image=g12,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal12)
    G12.place(x=130,y=300)
    G13=Button(Goals,image=g13,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal13)
    G13.place(x=230,y=300)
    G14=Button(Goals,image=g14,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal14)
    G14.place(x=330,y=300)
    G15=Button(Goals,image=g15,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal15)
    G15.place(x=430,y=300)
    G16=Button(Goals,image=g16,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal16)
    G16.place(x=530,y=300)
    G17=Button(Goals,image=g17,bg="#010220",bd=0,activebackground="#010220",command=OpenGoal17)
    G17.place(x=630,y=300)
    sdgss=Button(Goals,image=SDGss,bd=0,activebackground="#010220",command=Goals,highlightthickness=0)
    sdgss.place(x=820,y=325)



def OpenGoal1():
    webbrowser.open(linkGoal1)
def OpenGoal2():
    webbrowser.open(linkGoal2)
def OpenGoal3():
    webbrowser.open(linkGoal3)
def OpenGoal4():
    webbrowser.open(linkGoal4)
def OpenGoal5():
    webbrowser.open(linkGoal5)
def OpenGoal6():
    webbrowser.open(linkGoal6)
def OpenGoal7():
    webbrowser.open(linkGoal7)
def OpenGoal8():
    webbrowser.open(linkGoal8)
def OpenGoal9():
    webbrowser.open(linkGoal9)
def OpenGoal10():
    webbrowser.open(linkGoal10)
def OpenGoal11():
    webbrowser.open(linkGoal11)
def OpenGoal12():
    webbrowser.open(linkGoal12)
def OpenGoal13():
    webbrowser.open(linkGoal13)
def OpenGoal14():
    webbrowser.open(linkGoal14)
def OpenGoal15():
    webbrowser.open(linkGoal15)
def OpenGoal16():
    webbrowser.open(linkGoal16)
def OpenGoal17():
    webbrowser.open(linkGoal17)




def embeddedW():
    return

###############################################################################
###############################################################################
###############################################################################



def Listin():
    Lstory=randomStory
    Lgender=Voice.get()
    Lspeed=speedC.get()
    Voices=engine.getProperty('voices')
    def setvoice():
        if (Lgender=="Male"):
            engine.setProperty('voice', Voices[0].id)
            engine.say(Lstory)
            engine.runAndWait()
        else:
            engine.setProperty('voice', Voices[1].id)
            engine.say(Lstory)
            engine.runAndWait()

    if(Lspeed=="Fast"):
        engine.setProperty('rate',220)
        setvoice()
    elif(Lspeed=="Normal"):
        engine.setProperty('rate',150)
        setvoice()
    elif(Lspeed=="Slow"):
        engine.setProperty('rate',90)
        setvoice()

def StorygeneratorW():
    
    global Storygenerator_window
    global Voice
    global speedC
    Storygenerator_window=Toplevel(usermain)
    Storygenerator_window.geometry("1039x587+150+50")
    Storygenerator_window.resizable(False,False)
    Storygenerator_window.iconbitmap("photos\\neural.ico")
    Storygenerator_window.title("My graduation project")
    UM=Label(Storygenerator_window,image=story_image)
    UM.pack()
    L1=Label(Storygenerator_window,text=currentuser,fg="white",bg="#011A31",font=("tajawal",24,"bold"))
    L1.place(x=140,y=30)
    StoryButton=Button(Storygenerator_window,text="generate a story",command=storytextwindow,bg="#FF8A10",fg="white",font=("tajawal",18,"bold"))
    StoryButton.place(x=305,y=500)
    SDF=Frame(Storygenerator_window,width=750,height=300,bg="#011A31")
    SDF.place(x=35,y=150)
    AR=Label(Storygenerator_window,image=arrowright,highlightthickness=0,bd=0)
    AR.place(x=120,y=450)
    AL=Label(Storygenerator_window,image=arrowleft,highlightthickness=0,bd=0)
    AL.place(x=545,y=450)   
    LB=Button(Storygenerator_window,image=listen,highlightthickness=0,bd=0,activebackground="#00000F",command=Listin)
    LB.place(x=795,y=150)  
    V=Label(Storygenerator_window,image=voice,highlightthickness=0,bd=0)
    V.place(x=805,y=260)
    Voice=Combobox(Storygenerator_window,values=["Male","Female"],font="arial 14",state="r",width=17)
    Voice.place(x=810,y=320)
    Voice.set("Female")
    S=Label(Storygenerator_window,image=speed,highlightthickness=0,bd=0)
    S.place(x=805,y=400)
    speedC=Combobox(Storygenerator_window,values=["Fast","Normal","Slow"],font="arial 14",state="r",width=17)
    speedC.place(x=810,y=460)
    speedC.set("Normal")

def storytextwindow():
    global randomStory
    SF=Frame(Storygenerator_window,width=750,height=300,bg="#011A31")
    SF.place(x=35,y=150)
    stories=os.listdir("Stories")
    randomStoryfile=random.choice(stories)
    print(randomStoryfile)
    f=open("Stories\\"+randomStoryfile,"r")
    randomStory=str(f.read())
    f.close()
    fL=open("Labels\\"+randomStoryfile+"Label.txt","r")
    randomStoryLabel=str(fL.read())
    fL.close()  
    L1=Label(SF,text=randomStory,fg="white",font=("tajawal",14,"bold"),bg="#011A31",wraplength=700,anchor="se")
    L1.place(x=10,y=60)
    L2=Label(SF,text=randomStoryLabel,fg="white",font=("tajawal",18,"bold"),bg="#011A31")
    L2.place(x=200,y=20)



#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
def Login():
    global currentuser
    users=os.listdir("users")
    if(userL.get() in users):
        f= open("users\\"+userL.get(),"r")
        content=f.read().splitlines()
        f.close()
        if(passwordL.get() in content):
            currentuser=userL.get()
            Usermain()
        else:
            messagebox.showerror("Error","Incorrect Password")
    else:
        messagebox.showerror("Error","Incorrect Username")

         




#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################

def connecttodatabase():
    if(user.get()=="" or user.get()=="Username" or password.get()=="" or password.get()=="Password" or confirm.get()=="Confirm Password" or confirm.get()==""):
        messagebox.showerror("Error","All fields are required")
    elif(password.get()!=confirm.get()):
        messagebox.showerror("Error","Password mismatch!!")
    else:
        file=open("users\\"+user.get(),"w")
        file.write(user.get()+"\n")
        file.write(password.get()+"\n")
        file.close()
        user.delete(0,END)
        password.delete(0,END)
        confirm.delete(0,END)
        user.config(show="")
        password.config(show="")
        confirm.config(show="")
        user.insert(0,"Username")
        password.insert(0,"Password")
        confirm.insert(0,"Confirm Password")
        messagebox.showinfo("Success","Registeration success!!")

   
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################

def signup():
    global user
    global password
    global confirm
    global signupF
    signupF.destroy()
    signinF.destroy()
    aboutF.destroy()
    bi["image"]=SI
    signupF=Frame(root,bg="#4472C4",width=400,height=420)
    signupF.place(x=325,y=140)
    LSign=Label(signupF,text="Sign up",fg="black",bg="#4472C4",font=("Calibri",24,"bold"),bd=0,highlightbackground="#05051A")
    LSign.place(x=148,y=35)
    LSign=Label(signupF,text="join us now!!",fg="#FF8A10",bg="#4472C4",font=("arial black",16,"bold"),bd=0,highlightbackground="#05051A")
    LSign.place(x=120,y=72)
    ##################################################################################################################################################
    def enterusersignup(e):
        if(user.get()=="Username"):
            user.delete(0,"end")
    def leaveusersignup(e):
        if(user.get()==""):
            user.insert(0,"Username")

    user=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
    user.insert(0,"Username")
    user.place(x=40,y=130)
    user.bind("<FocusIn>",enterusersignup)
    user.bind("<FocusOut>",leaveusersignup)

    l1=Frame(signupF,height=2,bg="black",width=300)
    l1.place(x=40,y=161)
    ####################################################################################################################################################
    def enterPassword(e):
        if(password.get()=="Password"):
            password.config(show="*")
            password.delete(0,"end")
    def leavePassword(e):
        if(password.get()==""):
            password.insert(0,"Password")
            password.config(show="")

    password=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
    password.insert(0,"Password")
    password.place(x=40,y=195)
    password.bind("<FocusIn>",enterPassword)
    password.bind("<FocusOut>",leavePassword)

    l1=Frame(signupF,height=2,bg="black",width=300)
    l1.place(x=40,y=226)
    ####################################################################################################################################################
    def enterConfirm(e):
        if(confirm.get()=="Confirm Password"):
            confirm.config(show="*")
            confirm.delete(0,"end")
        
    def leaveConfirm(e):
        if(confirm.get()==""):
            confirm.insert(0,"Confirm Password")
            confirm.config(show="")

    confirm=Entry(signupF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
    confirm.insert(0,"Confirm Password")
    confirm.place(x=40,y=260)
    confirm.bind("<FocusIn>",enterConfirm)
    confirm.bind("<FocusOut>",leaveConfirm)

    l1=Frame(signupF,height=2,bg="black",width=300)
    l1.place(x=40,y=291)
    ####################################################################################################################################################

    def signinH(e):
        B1["font"]=("Calibri",14,"bold","underline")

    def signinN(e):
        B1["font"]=("Calibri",14,"bold")

    def hidePass():
        eyeP["image"]=unhide
        password.config(show="*")
        eyeP.config(command=showP)

    def hideCon():
        eyeC["image"]=unhide
        confirm.config(show="*")
        eyeC.config(command=showC)


    def showP():
        eyeP["image"]=hide
        password.config(show="")
        eyeP.config(command=hidePass)

    def showC():
        eyeC["image"]=hide
        confirm.config(show="")
        eyeC.config(command=hideCon)

    B2=Button(signupF,text="Sign up",fg="white",bg="#05051A",font=("Calibri",18,"bold"),width=22,activebackground="#05051A",activeforeground="#FF8A10",command=connecttodatabase)
    B2.place(x=40,y=325)
    Label(signupF,text="I have an account?",bg="#4472C4",fg="black",font=("Calibri",12,"bold")).place(x=80,y=385)
    B1=Button(signupF,text="Sign in",bg="#4472C4",fg="#FF8A10",font=("Calibri",14,"bold"),border=0,activebackground="#4472C4",command=signin)
    B1.place(x=220,y=380)
    B1.bind("<Enter>",signinH)
    B1.bind("<Leave>",signinN)
    unhide=PhotoImage(file="photos\\unhide.png")
    hide=PhotoImage(file="photos\\hide.png")
    eyeC=Button(signupF,image=unhide,border=0,borderwidth=0,bd=0,highlightthickness=0,activebackground="#4472C4",command=showC)
    eyeC.place(x=299,y=253)
    eyeP=Button(signupF,image=unhide,border=0,borderwidth=0,bd=0,highlightthickness=0,activebackground="#4472C4",command=showP)
    eyeP.place(x=299,y=188)

#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################

def signin():
    global userL
    global passwordL
    global signinF
    signupF.destroy()
    signinF.destroy()
    aboutF.destroy()
    bi["image"]=SI
    signinF=Frame(root,bg="#4472C4",width=400,height=420)
    signinF.place(x=325,y=140)
    LSign=Label(signinF,text="Sign in",fg="black",bg="#4472C4",font=("Calibri",24,"bold"),bd=0,highlightbackground="#05051A")
    LSign.place(x=148,y=35)

    ##################################################################################################################################################
    def enterusersignin(e):
        if(userL.get()=="Username"):
            userL.delete(0,"end")
    def leaveusersignin(e):
        if(userL.get()==""):
            userL.insert(0,"Username")

    userL=Entry(signinF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
    userL.insert(0,"Username")
    userL.place(x=40,y=130)
    userL.bind("<FocusIn>",enterusersignin)
    userL.bind("<FocusOut>",leaveusersignin)

    l1=Frame(signinF,height=2,bg="black",width=300)
    l1.place(x=40,y=161)
    ####################################################################################################################################################
    def enterPassword(e):
        if(passwordL.get()=="Password"):
            passwordL.config(show="*")
            passwordL.delete(0,"end")
    def leavePassword(e):
        if(passwordL.get()==""):
            passwordL.insert(0,"Password")
            passwordL.config(show="")

    passwordL=Entry(signinF,width=25,fg="black",border=0,bg="#4472C4",font=("Calibri",16))
    passwordL.insert(0,"Password")
    passwordL.place(x=40,y=195)
    passwordL.bind("<FocusIn>",enterPassword)
    passwordL.bind("<FocusOut>",leavePassword)

    l1=Frame(signinF,height=2,bg="black",width=300)
    l1.place(x=40,y=226)

    ####################################################################################################################################################
    ####################################################################################################################################################

    def signupH(e):
        B1["font"]=("Calibri",14,"bold","underline")
    def signupN(e):
        B1["font"]=("Calibri",14,"bold")

    def hidePass():
        eyeP["image"]=unhide
        passwordL.config(show="*")
        eyeP.config(command=showP)


    def showP():
        eyeP["image"]=hide
        passwordL.config(show="")
        eyeP.config(command=hidePass)



    B2=Button(signinF,text="Sign in",fg="white",bg="#05051A",font=("Calibri",18,"bold"),width=22,activebackground="#05051A",activeforeground="#FF8A10",command=Login)
    B2.place(x=40,y=325)
    Label(signinF,text="Don't have an account?",bg="#4472C4",fg="black",font=("Calibri",12,"bold")).place(x=60,y=385)
    B1=Button(signinF,text="Sign up",bg="#4472C4",fg="#FF8A10",font=("Calibri",14,"bold"),border=0,activebackground="#4472C4",command=signup)
    B1.place(x=230,y=380)
    B1.bind("<Enter>",signupH)
    B1.bind("<Leave>",signupN)
    unhide=PhotoImage(file="photos\\unhide.png")
    hide=PhotoImage(file="photos\\hide.png")

    eyeP=Button(signinF,image=unhide,border=0,borderwidth=0,bd=0,highlightthickness=0,activebackground="#4472C4",command=showP)
    eyeP.place(x=299,y=188)

#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
    

def about():
    global aboutF
    signupF.destroy()
    signinF.destroy()
    aboutF.destroy()
    bi["image"]=SI
    





#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################


def home():
    global signupF
    global signinF
    bi["image"]=BI
    bi.pack()
    signinF.destroy()
    signupF.destroy()
    aboutF.destroy()


#######################################################################################################################################################################################################
#######################################################################################################################################################################################################
#######################################################################################################################################################################################################






def loginH(e):
    lH=PhotoImage(file="photos\\lh.png")
    L["image"]=lH
    L.image=lH
    L.place(x=728,y=0)
def loginN(l):
    l=PhotoImage(file="photos\\llll.png")
    L["image"]=l
    L.image=l
    L.place(x=728,y=0)
def AboutH(e):
    aH=PhotoImage(file="photos\\Ah.png")
    A["image"]=aH
    A.image=aH
    A.place(x=570,y=0)
def AboutN(l):
    a=PhotoImage(file="photos\\A.png")
    A["image"]=a
    A.image=a
    A.place(x=570,y=0)
def signupH(e):
    SH=PhotoImage(file="photos\\sh.png")
    S["image"]=SH
    S.image=SH
    S.place(x=885,y=0)
def signupN(l):
    s=PhotoImage(file="photos\\s.png")
    S["image"]=s
    S.image=s
    S.place(x=885,y=0)
def homeH(e):
    hH=PhotoImage(file="photos\\hh.png")
    H["image"]=hH
    H.image=hH
    H.place(x=408,y=0)
def homeN(l):
    h=PhotoImage(file="photos\\H.png")
    H["image"]=h
    H.image=h
    H.place(x=408,y=0)








First.mainloop()

