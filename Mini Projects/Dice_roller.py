import random

dice = { 
    1 : ("┌─────────┐", 
         "│         │", 
         "│    ●    │", 
         "│         │", 
         "└─────────┘" ),

    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘" ),

    3 : ("┌─────────┐",
         "│       ● │",
         "│    ●    │",
         "│ ●       │",
         "└─────────┘" ),
    4 : ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘" ),
    5 : ("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘" ),
    6 : ("┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘" )
}
d = []
total = 0
no_of_dice = int(input("How many times do you want to roll the dice? "))

for i in range(no_of_dice):
    d.append(random.randint(1, 6))

for i in range(no_of_dice):
    for line in dice.get(d[i]):
        print(line)

for i in d:
    total += i
    print(f"total = {total}")
