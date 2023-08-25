# GUI means graghical user interface
from tkinter import *
from tkinter import messagebox

#Create the main app window
age_app = Tk()      #the main window in inside the TK GUI
#run the app infinitly

age_app.title("Amideast age app")
#setting the window dimentions
age_app.geometry("400x200")
#Write text (lable for the app)
the_text = Label(age_app, text="Write your age", height=1, font=("Arial", 20))
the_text.pack() #place the text in the main window
# create input for the age
# age variables
age= StringVar()
#set default value
age.set("00")
#ask for the input
age_input= Entry(age_app, width=2, font=("Arial"), textvariable=age) # where are you going to put the age_put, sure in the age_app
age_input.pack()    #put the age input inside the main window
def calc():
    # Get the age that the user wrote
    the_age_value=age.get()
    months= int(the_age_value)*12
    weeks= months*12
    days= int(the_age_value)*365

    line_one = f"Your age in months is :{months}"
    line_two = f"Your age in weeks is :{weeks}"
    line_three = f"Your age in days is :{days}"
    all_lines=[line_one,line_two,line_three]
    print(all_lines)
    messagebox.showinfo("your age in months, weeks and days", "\n".join(all_lines) )


# Create the buttion for calculate the age
Calc_Button=Button(age_app, text="calculate the age", width=20, height=2, background="#e91e63", fg="white", borderwidth=0, command=calc)
Calc_Button.pack() #put the button in the main window
age_app.mainloop()
# Change app title
# to generate exe file we should first instal pip install pyinstaller
# write in the power shell pip install auto-pt-to-exe
# open auto-py-to-exe
#then convert it throught the program