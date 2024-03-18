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


input("Press enter to close")
