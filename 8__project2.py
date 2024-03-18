import math

def newton(x, estimate, tolerance):
    estimateTwo = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)

    if difference <= tolerance:
        return estimate
    else:
        return newton(x, estimateTwo, tolerance)    

def main():
    while True:
        x = float(input("Please enter a positive number: "))
        estimate = 1.0
        tolerance = 0.000001
        newton(x, estimate, tolerance)

        estimate = newton(x, estimate, tolerance)
        
        print("The programs estimate: ", estimate)
        print("Pythons estimate: ", math.sqrt(x))

        question = input("Enter any letter or number to enter a new number or hit the 'enter' button to exit: ") # Question to determine whether the user wants to continue inputting new numbers or to exit the program

        if not question:                              # Determines whether the user hit the enter button and, if so, then prints an exit message and then breaks the loop
            print("Thank you for using this program.")
            break

        else:       # If the user enters any key that gives a value then it will continue the loop
            continue
if __name__ == "__main__":
    main()


