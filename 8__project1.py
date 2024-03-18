import math

def newton(): 
    x = float(input("Please enter a positive number: ")) 
    tolerance = 0.000001
    estimate = 1.0

    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)

        if difference <= tolerance:
            break

    print("The programs estimate: ", estimate)
    print("Pythons estimate: ", math.sqrt(x)) 

def main():
    while True:
        newton()

        question = input("Enter any letter or number to enter a new number or hit the 'enter' button to exit: ") # Question to determine whether the user wants to continue inputting new numbers or to exit the program

        if not question:                              # Determines whether the user hit the enter button and, if so, then prints an exit message and then breaks the loop
            print("Thank you for using this program.")
            break

        else:       # If the user enters any key that gives a value then it will continue the loop
            continue
if __name__ == "__main__":
    main()
