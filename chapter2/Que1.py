# Write a python program to add two numbers. 
a=45
b=56
c=a+b
print(c)

#2. Write a python program to find remainder when a number is divided by z. 
a=34
b=5
print("Remainder when a is divided by b: ", a % b)

# 3. Check the type of variable assigned using input () function. 

a = input("enter value of a:")
print(type(a))
 # see type of variable of input function is always variable unless we give manually type of input 
 #for example int(input("enter variable :")) 

a = int(input("enter a:"))
print(type(a))

#now the output will be int 

# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80 

a = 34
b = 80

c = a>=b
print(c)

a = 34
b = 80

if a>b:
    print("a is greater then b")
else:
    print("b is greater")

# 5. Write a python program to find an average of two numbers entered by the user. 
a = int(input("enter a :"))
b = int(input("enter b :"))
average=(a+b)/2
print("avearge is : ",average)

# 6. Write a python program to calculate the square of a number entered by the user.

a = int(input("enter a : "))
square=a*a
print("square of given number is : ",square)



