'''
Rock = 1
Paper = -1
Scissors = 0

'''
import random

computer = random.choice([1, -1, 0])


youStr = (input("Enter your choice: "))
youDict = {"r": 1, "p":-1, "s": 0}
reverseDict ={1: "Rock", -1:"Paper", 0:"Scissors"}
you = youDict[youStr]
print(f"Your choice is: {reverseDict[you]}, Computer's choice is: {reverseDict[computer]}")
if(computer==you):
    print("Draw!!")
else:
    if(computer==-1 and you==0):
        print("You won!!")
    elif(computer==-1 and you==1):
        print("You lose!!")
    elif(computer==1 and you==-1):
        print("You won!!")
    elif(computer==1 and you==0):
        print("You lose!!")
    elif(computer==0 and you==-1):
        print("You won!!")
    elif(computer==0 and you==1):
        print("You lose!!")
    else:
        print("Something went wrong")
    


