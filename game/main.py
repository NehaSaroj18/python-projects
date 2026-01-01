# PROJECT 1: SNAKE, WATER, GUN GAME 
# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user.

# 1 for snake 
# -1 for water
# 0 for gun


import random
computer= random.choice([-1,0,1])
youstr=input("Enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water" , 0:"Gun"}

you = youDict[youstr]
print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("Draw")

else:
     if((computer-you)==2 or (computer-you)== -1):
          print("YOU WIN !")
     else:
          print("YOU LOSE!!")

# else: 
#     if (computer == -1 and you == 1): -2
#         print("You Win!")

#     elif(computer == -1 and you == 0):-1
#          print("You Lose")

#     if(computer == 1 and you == -1):2
#          print("You loose")

#     elif(computer == 1 and you == 0):1
#          print("You win")

#     if(computer == 0 and you == 1):1
#          print("You loose")

#     elif(computer == 0 and you == -1):1r
#          print("You Win")

#     else:
#         print("Something went wrong")
