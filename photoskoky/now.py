#While loop ask for condition if it is true the loop will run, if not the code will not run
a=0
while a < 10:
    print(a)
    a+=1
else:
    print("the loop ends")
###################################################
myf1=["as", "ah","an", "am","aj", "ak","al", "ai","ao", "ap",]
print(myf1[0])
print(myf1[1])
print(myf1[2])
print(myf1[3])
print(myf1[4])
print(myf1[5])
print(myf1[6])
print(myf1[7])
print(myf1[8])
print(myf1[9])
print(myf1[10])
myf2=["as", "ah","an", "am","aj", "ak","al", "ai","ao", "ap",]
print(len(myf2))
a=0
while a < len(myf2):
    print(f"{str(a+1).zfill(2)}-{myf2[a]}")
    a+=1
else:
    print("the list ends")
#the following example is on the bookmarks manager
myfavwebsites=[]
maximumwebsites=5
while maximumwebsites>0:
    web=input("what is the website that you like to add: ")
    myfavwebsites.append({web.strip().lower()})
    maximumwebsites-=1
    print("websitesadded")
    print(f"there is {maximumwebsites} places left")
    print(myfavwebsites)
else :
    print("book mark is full")
####################################################################
#paswword gusser
tries= 4
mainpassword= "ammar@123"
inputpassword= input("what is your password: ") 
while inputpassword != mainpassword:
    tries-=1
    print(f"wrong password,{tries} chances left")
    inputpassword= input("what is your password: ") 
    if tries== 0:
        print("you finished all of your tries")
        break
else:
    print("your password is true")
####################################################################
mynumbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in mynumbers :
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")
else:
    print("loop is finished")
myname8= "ammar"
for letter in myname8:
    print(letter.upper())
####################################################################
Myrange = range(1, 101)
for number in Myrange:
    print(number)
############################################################
myskills= {
"HTML" : "90%",
"C#" : "70%",
"PYTHON" : "90%",
"JAVASCRIPT" : "80%",
"FLUTER" : "70%"
}
print(myskills["HTML"])
print(myskills.get("HTML"))
for skill in myskills:
    print(f"my progress in lang {skill} is {myskills[skill]}")
#########################################################################
newlist=[1, 3, 5, 7, 9, 11, 13, 15, 17]
for numbers in newlist:
    if number ==13:
        continue
    print(number)
#########################################################################
newlist2=[1, 3, 5, 7, 9, 11, 13, 15, 17]
for numbers in newlist:
    print(number)
    if number ==13:
        break
    print(number)
#########################################################################
newlist3=[1, 3, 5, 7, 9, 11, 13, 15, 17]
for numbers in newlist:
    print(number)
    if number ==13:
        pass     # if you wantt to pass the code and then back again for it and activate it
    print(number) 
#########################################################################
#funcions are the most important concept in the language
#1 function run when you call it
#2 function can return data or can do the task without returning data.
#3 function do specific task
#4 functions accept elements t deal with (parameters)
#5 functions do its tasks to the arguments (elements inside our code)
#6 function do its task to all the app 
#7 youcal call the function when ever you want
def function_name():
    print("hello python from inside the function") 
  #########################################################################
def function_name1():
    print("hello python from inside the function") 
function_name1()
 #########################################################################
def functionname3():
    return "hello python from inside the function"
print(functionname3())
variable= functionname3()
print(variable)
###################################################################
a, b, c= "ahmed", "ammar", "khaled"
# print(f" hello{b}")
# print(f" hello{b}")
# print(f" hello{b}")
def say_hello(the_name):
    print(f"hello{the_name}")
say_hello(a)
# def                          function keyword
#say_hello                     function name
#the_name                      parameter
#print(f"hello{the_name}")     task
#khaled                        argument(what we do the task on)
######################################################################
var1=int(input("inter the first number: "))
operation= input("choose the operation: ")
var2=int(input("inter the second number: "))
if operation == "add":
    print(var1 + var2)
elif operation == "sub":
    print(var1 - var2)
elif operation == "div":
    print(var1 / var2)
elif operation == "mul":
    print(var1 * var2)
else:
    print("wrong operator please try again")
######################################################################
def add(n1, n2):
  return n1 + n2

var1=int(input("inter the first number: "))
operation= input("choose the operation: ")
var2=int(input("inter the second number: "))
if operation == "add":
    add(var1, var2)
else:
    print("thank you for using our calculator")
#######################################################################
def add(n1, n2):    
   # This function is used for adding two numbers   
   return n1 + n2   
def subtract(n1, n2):   
   # This function is used for subtracting two numbers   
   return n1 - n2   
def multiply(n1, n2):   
   # This function is used for multiplying two numbers   
   return n1 * n2   
def divide(n1, n2):   
   # This function is used for dividing two numbers    
   return n1 / n2    
# Now we will take inputs from the user    
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
operation = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if operation == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif operation == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
elif operation == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
elif operation == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")  
