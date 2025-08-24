# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 

name=input("enter your name:")
print(f"Good afternoon , {name}")



# 2. Write a program to fill in a letter template given below with name and date. 

letter = '''  Dear <|Name|>, 
You are selected! <|Date|> ''' 
print(letter.replace("<|Name|>", "neha").replace("<|Date|>","24 August"))

# 3. Write a program to detect double space in a string. 


name="hare krishna hare   krishna krishna krishna hare hare"
print(name.find(" "))
print(name.replace("  "," "))

# 5. Write a program to format the following letter using escape sequence 
# characters. 
letter = "Dear Harry,\t this python course is nice.\n Thanks!" 
print(letter)