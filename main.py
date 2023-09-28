MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
                print("Please enter in a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet. (1-" + str(MAX_LINES)+ ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <=MAX_LINES :
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter in a number.")
    return lines

def get_bets():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
                print("Please enter in a valid number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bets()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bets is equal to: $:{total_bet}")


main()

