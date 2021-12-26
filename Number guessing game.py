#Number Guessing Game using random
import random
winning_number = random.randint(1,100)
guess_number = int(input("Guess the number:"))
guess = 1
game_over = False


while not game_over:
    if guess_number == winning_number:
        print(f"You Win!!!,You guessed this number in {guess} times")
        game_over = True
    else:
        if guess_number < winning_number:
            print("too low")


        else:
            print("too high")

        guess += 1
        guess_number = int(input("Guess again: "))