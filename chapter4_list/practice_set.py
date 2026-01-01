# 1. Write a program to store seven fruits in a list entered by the user. 
fruits = []

f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)
f1=input("Enter fruit name : ")
fruits.append(f1)

print(fruits)


# 2 Write a program to accept marks of 6 students and display them in a sorted manner. 

marks=[]

mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)
mark=float(input("enetr your marks:"))
marks.append(mark)


marks.sort()
print(marks)

# 3. Check that a tuple type cannot be changed in python.

a=(1,2,3)
print(type(a))

# 4. Write a program to sum a list with 4 numbers. 

l=[3,4,5,6,6]
print(sum(l))

# 5. Write a program to count the number of zeros in the following tuple: 
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
n=a.count(0)
print(n)

