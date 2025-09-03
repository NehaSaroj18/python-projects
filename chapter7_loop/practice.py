# 1. Write a program to print multiplication table of a given number using for loop. 

# mul=int(input("enter number for multiplication table :"))
# for i in range(1,11):
#     print(f"{mul} x {i} = {mul*i}")

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# 3. Attempt problem 1 using while loop. 

# mul=int(input("enter number for multiplication table :"))
# i=1
# while(i<=10):
#     print(f"{mul} x {i} = {mul*i}")
#     i+=1

# 4. Write a program to find whether a given number is prime or not. 

# i=int(input("enter number :"))

# for prime in i:
#     if(prime%prime== 0 and prime%1==0):
#         print(f"number is prime {num}")


# n = int(input("enter a number :"))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("number is not prime")
#         break
#     else:
#         print("Number is prime")

# 5. Write a program to find the sum of first n natural numbers using while loop.
# n = int(input("enter a number :"))
# fact*=i
# n=int(input("enter a number"))
# i=1
# fact=1

# while(i<=n):
#     fact*=i
#     i+=1

# print(fact)

# n=int(input("enter number :"))
# fact=1

# for i in range(1, n+1):
#     fact*=i

# print(f"factorial of {n} is {fact}")
 
# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3 

# n=3
# i=1
# while(i<=n):
#     print("*")
#     i*=1


# n=int(input("enter number :"))

# for i in range(1, n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

# 9. Write a program to print the following star pattern. 
# *** 
# * *   for n = 3 
# ***  

# n=int(input("enter number :"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*",end="")
#         print(" "* (n-2),end="")
#         print("*", end="")
#     print("")

# 10. Write a program to print multiplication table of n using for loops in reversed order. 

n=int(input("Enter number : "))
 
for i in range(1, 11):
    print(f"The table {n}x{i} = {n*i} ")
    
