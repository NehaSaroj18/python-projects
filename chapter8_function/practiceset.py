#1. Write a program using functions to find greatest of three numbers. 
def greatestno(num1 ,num2 ,num3):
    if(num1>num2 and num2>num3):
        print(f"num1 is gratest : {num1} ")
    elif(num2>num1 and num2>num2):
        print(f"num2 is gratest : {num2}")
    else:
        print(f"num3 is greatest : {num3}")
    
greatestno(1,2,4)
print("thank you")

def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>c):
        return b
    else:
        return c
    
a=2
b=5
c=9

print(gratest(a,b,c))

# 2. Write a python program using function to convert Celsius to Fahrenheit. 
c=5*(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9

f=int(input("Enter temp : "))
c=f_to_c(f)
print(f"{round(c,2)} 'c")

# 3. How do you prevent a python print() function to print a new line at the end. 

print("a")
print("a")
print("a")
print("a",)
print("a",end="")
print("a",end="")#end string appended after the last value, default a newline (do not give newlines)


#4. Write a recursive function to calculate the sum of first n natural numbers. 
'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4

sum(n)=1+2+3+4+5....n-1+n
sum(n)=sum(n-1)+n

'''
def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n #n=3 =1+2+3
print(sum(4))       


'''
Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3
'''

def pattern(n):
    if n==0:
        return
    print("*"*n)   
    pattern(n-1)

pattern(3)


def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-2)

pattern(3)

# 6. Write a python function which converts inches to cms. 
# 1cm 2.54

def inch_to_cms(inch):
    return inch*2.54

n=int(input(f"Enter inches :"))
print(f"the coreespoinding value in cms is :  {inch_to_cms(n)}")

# 7. Write a python function to remove a given word from a list ad strip it at




def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word)) #In Python, strip() is a built-in string method. It removes whitespace (spaces, tabs, newlines) from the beginning and end of a strin


l=["Radhe","Raman","Ram","Kanha","Sita","an"]

print(rem(l,"an"))

#8. Write a python function to print multiplication table of a given number. 

def mul(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter number: "))
mul(n)   # no need to print return value

def multiplication(n):
    for i in range(1,11):
        print(f"{n}x{i} = {n*i}")
multiplication(7)