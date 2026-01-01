'''
RECURSION 
Recursion is a function which calls itself. 
It is used to directly use a mathematical formula as function
factorial(n) = n x factorial (n-1) 
'''
def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int(input("enter a number : "))
print(f"the factorial of this is : {fact(n)}")