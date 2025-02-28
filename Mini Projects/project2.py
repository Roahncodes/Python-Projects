import random

random_number = random.randint(1, 100)   
a = -1
guesses = 0

while(a != random_number):
    a = int(input("Enter a number: "))
    guesses+=1
    if(a > random_number):
      
     print("Lower number please")
    else:
     print("Higher  number please")
    


print(f"You guesses the  number in {guesses} attempt")
