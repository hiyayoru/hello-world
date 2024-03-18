import random
import math

smallNumber = int(input("Enter the smaller number: "))
largNumber = int(input("Enter the larger number: "))

# Calculate the minimum number of guesses needed
minimumGuesses = math.ceil(math.log(largNumber - smallNumber + 1, 2))

count = 0
while True:
    count += 1
    guess = random.randint(smallNumber, largNumber)
    print("Computers guess:", guess)
    
    computerGuess = input("Is the guess too small (enter small), too large (enter large), or correct (enter correct)?: ").lower()
    
    if computerGuess == "small":
        smallNumber = guess + 1
    elif computerGuess == "large":
        largNumber - 1
    elif computerGuess == "correct":
        if count == minimumGuesses:
            print("Congratulations! The computer guessed it in exactly", count, "tries!")
        else:
            print("Congratulations! The computer guessed it in", count, "tries!")
        break
    else:
        print("Invalid input. Please enter 'small', 'larg', or 'correct'.")
