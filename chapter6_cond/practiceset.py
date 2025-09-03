# 1. Write a program to find the greatest of four numbers entered by the user. 
num1=int(input("enter the number 1 :"))
num2=int(input("enter the number 2 :"))
num3=int(input("enter the number 3 :"))
num4=int(input("enter the number 4 :"))

if(num1>num2 and num1>num3 and num1>num4):
    print("Greatest number is num1:",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("Greatest number is num2:",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("Greatest number is num3:",num3)
elif(num4>num1 and num4>num2 and num4>num3):
    print("Greatest number is num4:",num4)
else:
    print("Not valid number")

print("Successfully RUN !")

# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

marks=(input("Enter your marks by order of subjects : "))
sub1=float(input("Enter marks PHYSICS :"))
sub2=float(input("enter marks CHEMISTRY :"))
sub3=float(input("Enter marks LANGUAGE :"))

if( sub1>=33 and sub2>=33 and sub3>=33):
    print("PASS")
else:
    print("FAIL")


# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 

keyword=input("enter ypur comment")
if(keyword == "neha" and keyword ==  "Make lot of money " and keyword == "buy now" and keyword == "subscribe this" and keyword == "click this" ):
    print("spam comment ")
else:
    print("THANKS !")

user=input("Enter username :")

if(len(user)<=10):
    print("your username contains less than 10 charchaters")
else:
    print("Well Done !")

# 5. Write a program which finds out whether a given name is present in a list or not.

l=["Kanha","Radhe","Neha","Meera","Rukmni"]

name=input("Enter your name : ")

if(name in l):
    print("Your name is in list")
else:
    print("Name is not in present list")
    print("Contact to Admin")

# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 


# marks=float(input("Enter tour marks :"))


if(marks>90 and marks<=100):
    print("A+")
elif(marks>80 and marks<=90):
    print("A")
elif(marks>70 and marks<=80):
    print("B")
elif(marks>60 and marks<=70):
    print("C")
elif(marks>50 and marks<=60):
    print("D")
else:
    print("FAIL !")

print("DONE !!")

# another way

marks=float(input("Enter tour marks :"))

if(marks>90 and marks<=100):
    grade = "A+"
elif(marks>80 and marks<=90):
    grade = "A"
elif(marks>70 and marks<=80):
    grade = "B"
elif(marks>60 and marks<=70):
    grade = "C"
elif(marks>50 and marks<=60):
    grade = "D"
else:
    print("FAIL !")

print("Your grade is : ",grade)


# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post=input("Create your post :")

if("kanha".lower() in post.lower()):
    print("knaha in post !")
else:
    print("kanha is not in post")