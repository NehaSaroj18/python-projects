#A function is a group of statements performing a specific task. 
# we can call function to do the same things for infinte time you want to do by just calling 




#function defintion
def avg():
    a = int(input("enter number :"))
    b = int(input("enter number :"))
    c = int(input("enter number :"))

    average = (a+b+c)/3
    print(average)
    print(f"this is function : {average}")

    # Python isolates function variables on purpose:
    # To avoid conflicts (two functions can use the same variable name without interfering).
    # To keep code clean and modular (functions are like “black boxes”).

#function call
avg()
print(f"this is function : {average}") #because outside the function, Python doesn’t know what average is.
avg()

# there is another way to so this
def avg():
    a = int(input("enter number :"))
    b = int(input("enter number :"))
    c = int(input("enter number :"))

    average = (a+b+c)/3
    return average   # send the value back

result = avg()  # store the returned value
print(result)   # now works fine outside



# TYPES OF FUNCTIONS IN PYTHON 
# There are two types of functions in python: 
# • Built in functions (Already present in python) 
# • User defined functions (Defined by the user) 
# Examples of built in functions includes len(), print(), range() etc. 
# The func1() function we defined is an example of user defined function.