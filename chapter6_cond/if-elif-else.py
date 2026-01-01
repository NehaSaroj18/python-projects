#Write a program to print yes when the age entered by the user is greater than or equal to 18.
age = int(input("enter age : "))
if(age>=18):
    print("yes") # the space which come after ":" (colon) enter is called as indentation
elif(age<0):                # the space specifies that we indent the program or entered in if(loop)
    print("you are entering invalid age")
else:
    print("NO")

print("End of the program !") #this is not in any loop it will run in any condition