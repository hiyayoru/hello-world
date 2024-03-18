import random #Importing random to ensure the test numbers are random each time
import statistics #Importing statistics in order to use mode()  

def main():
    givenNumbers = []
    listLength = 7 # limits the amount of numbers generated to 7
    for num in range(listLength): # generates random numbers and appends it to givenNumbers
        randomNum = random.randint(1, 10)
        givenNumbers.append(randomNum)
    print("The ranomdized test numbers are: ", givenNumbers) 
    print("Mean: ", mean(givenNumbers))
    print("Median: ", median(givenNumbers))
    print("Mode: ", mode(givenNumbers))


def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
    

def median(numbers):
    numbers.sort() # sorting the numbers from smallest to largest
    if not numbers:
        return 0
    if len(numbers) % 2 == 1: 
        return numbers[len(numbers) // 2] # if the list is odd numbered, this will return the middle number
    else: 
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2 #if the list is even, returns the average of the two middle numbers

def mode(numbers):
    if not numbers:
        return 0
    return statistics.mode(numbers) # Used mode() from the module statistics to calculate the mode of the random numbers

if __name__ == "__main__":
    main()
