import sys

while True:
    
    newVideoPrice = 3.00
    oldVideoPrice = 2.00

    newVideoNumber = int(input("Please enter the total number of new videos: "))
    oldVideoNumber = int(input("Please enter the total number of old videos: "))
    numberOfNights = int(input("Please enter the total number of nights rented: "))

    newVideoCalculation = newVideoPrice * newVideoNumber
    oldVideoCalculation = oldVideoPrice * oldVideoNumber

    combinedCost = newVideoCalculation + oldVideoCalculation

    totalCost = combinedCost * numberOfNights

    print("The total cost for", numberOfNights, "nights is: $" +str(totalCost))

    loopQuestion = input("Would you like to calculate another sale? (yes/no): ")
    if loopQuestion.lower() == 'yes':
        continue
    else:
        input("Thank you for using this program. Press enter to close...")
        sys.exit()
