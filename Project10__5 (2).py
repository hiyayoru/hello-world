import sys

while True:
    sideA = int(input("Enter the length of side A: "))
    sideB = int(input("Enter the length of side B: "))
    sideC = int(input("Enter the legnth of side C: "))

    if sideA == sideB == sideC:
        print("This IS a equilateral triangle.")
    else:
        print("This is NOT a equilateral triangle.")

    question = input("Enter 'yes' if you'd like to input new numbers or 'exit' to leave the program.")
    if question == 'exit':
        print("Thank you for using our program.")
        sys.exit()
