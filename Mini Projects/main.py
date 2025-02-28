import sys
import random

MAX_LINES = 3
MAX_BET = 1000
ROWS = 3
COLS = 3

SC = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, count in symbol.items():
        all_symbols.extend([symbol] * count) 

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) 
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()  

def deposit():
    while True:
        try:
            amt = int(input("Choose a number to be deposited: $"))
            if amt > 0:
                return amt
            else:
                print("Enter a valid amount.")
        except ValueError:
            print("Please enter a valid number.")

def getting_no_of_lines():
    while True:
        try:
            lines = int(input(f"Choose number of lines (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        except ValueError:
            print("Please enter a valid number.")

def bet_amt(balance, lines):
    while True:
        try:
            bet = int(input(f"Choose the amount you want to bet per line (Max ${MAX_BET}): $"))
            total_bet = bet * lines
            if 1 <= bet <= MAX_BET and total_bet <= balance:
                return bet
            else:
                print(f"Invalid bet. Ensure it's between $1 and ${MAX_BET}, and within balance.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    balance = deposit()
    
    while True:  
        print(f"Current Balance: ${balance}")
        lines = getting_no_of_lines()
        bet = bet_amt(balance, lines)
        total_bet = bet * lines

        balance -= total_bet
        print(f"\nTotal bet: ${total_bet}")
        print(f"Remaining balance: ${balance}")

        slot = get_machine_spin(ROWS, COLS, SC)
        print("\nSlot Machine Result:")
        print_slot_machine(slot)

        if balance <= 0:
            print("You're out of balance! Game over.")
            break

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
