# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it u

# words = {
#     "namste":"hello",
#     "chai":"tea",
#     "panipuri":"water balls",
#     "aankhe":"eyes"
# }

# word = input("enetr the word for english translation :")
# print(words[word])

 #by this if user enter input namste they will gate hello 
#there is some issues that we have to take exact values  as given in key while taking user iput we can't give sapce 
#otherwisw this will give error


# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).


# s=set()

# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)
# number = int(input("Enter eight numbers"))
# s.add(number)

# print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

# s = set()
# s.add(18)
# s.add("18")

# print(s) # this will add both because one is int and other is string


# What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')
s.add("neha")

print(len(s)) #this will give length 3 na ki 4 kyuki agar value same hai to python ko datatype se fark nhi padta


# 5. s = {} 
# What is the type of 's'? 

s = {}
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

d = {}
name = input("Enter friend's name :")
lang = input("Enter favourite laguage:")
d.update({name:lang})
name = input("Enter friend's name :")
lang = input("Enter favourite laguage:")
d.update({name:lang})
name = input("Enter friend's name :")
lang = input("Enter favourite laguage:")
d.update({name:lang})
name = input("Enter friend's name :")
lang = input("Enter favourite laguage:")
d.update({name:lang})

print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# value can be same but key cant be same because key is identifier

# 8. If languages of two friends are same; what will happen to the program in problem 6?
# = nothing will happen value can be same 


# 9.Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]}
s[4][0]=9 

# first thing we can't include list in set
# because sets in python require all their elements to be immutable and hashable


