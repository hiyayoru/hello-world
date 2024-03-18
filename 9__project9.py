from functools import reduce # import reduce specifically

def numberSum(numbers): # calculates the sum of the numbers

    return reduce(lambda x, y: x + y, numbers) 

def readFile(filename): # function that gets all the necessary information from the file

    fileNameQuestion = input("Enter the name of the file you wish to open: ") # Asks the user what file they want to open

    with open(fileNameQuestion, 'r') as file:
        numbers = map(float, file.read().split())
    return numbers

def average(numbers): # function to determine average 

    sum = numberSum(numbers)

    count = len(numbers) # count the number of terms within the file

    if count == 0: # if there are no terms in the file return a 0
        return 0
    else:
        return sum / count # average caluclation

def main(filename): # main function

    numbers = readFile(filename) # assigns the readFile fucntion to 'numbers'
    nList = list(numbers) # turns 'numbers' into a list and assigns it to nList (short for numberList)

    print("Numbers found within file: ", nList) # prints off the numbers found within the file to show the user what those numbers are
    print("Average:", average(nList)) # prints the average


while True: # Simple loop to deteremine whether the user wants to calculate the average from a different file
    
    main('test.txt') # calls the main function

    question = input("Would you like to calcuate the average of a new file? (yes/no): ")
    if question.lower() == 'yes':
        continue
    else:
        input("Press enter to close program...")
        break
