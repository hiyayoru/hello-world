import random # Importing the random module in order to create a random list of numbers within main()



def isSorted(numberList): # function responsible for the calculation of the program
    if len(numberList) <= 1: # reads the length of the list and determines whether its automatically true based on how many numbers is in the list
        return True
    for i in range(len(numberList) - 1): 
        if numberList[i] > numberList[i + 1]: # reads the list and checks each 'pair' of numbers to determine whether the list is false
            return False
    return True


def main(): # Main function of the program that contains the various outputs and questions needed for the program

    question = input("Do you want to use randomly generated numbers or a predetermined list? (enter list or random): ") # Initial question that determines whether the number the user wants to use is predetermined or random

    if question.lower() == 'list': # If statement for if the user enters 'list'

        question2 = int(input("Enter a number between 1-3: ")) # Question that determines which predetermined list to use

        if question2 == 1: # if statement for the first predetermined list
            numberList = [1, 5, 8, 10, 15]
            print("Predetermined numbers: ", numberList) # prints the numbers used so the user can see why the program returned the result

        elif question2 == 2: # elif statement for the second predetermined list
            numberList = [5, 32, 48, 3, 9]
            print("Predetermined numbers: ", numberList)# prints the numbers used so the user can see why the program returned the result

        elif question2 == 3: # elif statement for the third predetermined list
            numberList = [2, 0, 1, 34, 6]
            print("Predetermined numbers: ", numberList)# prints the numbers used so the user can see why the program returned the result

        isSorted(numberList) 
        print(isSorted(numberList))

    else: # else statement for the random generation of a numbered list
        print("Generating random list of numbers...")
        numberList = random.sample(range(15), 5) # generates a random list of 5 numbers that ranges from 0 to 15

        isSorted(numberList)
        
        print(isSorted(numberList))
        print("Generated numbers: ", numberList)

while True: # Basic loop 
    main() # Calling the main function

    loopQuestion = input("Would you like to go again? (yes/no): ") # Loop question determines whether the user wants to go again
    if loopQuestion.lower() == 'yes':
        continue
    else:
        input("Press enter to end program...")
        break
