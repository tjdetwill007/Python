import random
number = random.randint(1,10)
def guess_game():
    guess= int(input("Please guess a number between 1 to 10 : "))
    while guess!= number:
        if guess > number and guess < 11:
            print("Selected number is greater than random number")
            guess= int(input("Please retry : "))
        elif guess < number and guess < 11:
            print("Selected number is samller than random number")
            guess= int(input("Please retry : "))
        else:
            guess= int(input("Please enter the valid number between 1 and 10 : "))
    print("Congratulations! you won the game")
guess_game()

