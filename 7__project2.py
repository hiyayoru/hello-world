
fileName = input("Enter the name of the file: ")

with open(fileName, 'r') as f: # opens fileName, reads it, and assigns it to 'f'
    lines = f.readlines() # reads the lines of 'f' and assigns it to 'lines'
        

numberOfLines = len(lines) # counts the number of lines in 'lines'

while True:
    print("The number of lines in the file: ", numberOfLines) # prints the number of lines
    lineNumber = input("Enter a line number: ") # asks user for a line number

    if not lineNumber.isdigit(): # If the line number isn't a digit, it asks the user to input a number 
        lineNumber = input("Invalid character. Please enter a line NUMBER: ")

    lineNumber = int(lineNumber)

    if lineNumber == 0:  # if the number entered is zero, it leaves the program
        print("Leaving program...")
        break
    elif lineNumber < 0 or lineNumber > numberOfLines: # if the number entered is higher than the number of lines, then it asks for a new number to input
        print("Invalid line number. Enter a number between 1 and", numberOfLines)

    else: # 
        print("Line", lineNumber, ":", lines[lineNumber - 1]) # Prints off the line


