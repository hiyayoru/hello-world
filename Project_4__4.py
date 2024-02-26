initialHeight = float(input("Enter the height the ball was dropped from: "))

numberOfBounces = int(input("Enter how many times you want the ball to bounce: "))

bounciness = 0.6

distanceTravelled = 0

nextBounce = initialHeight

for i in range(numberOfBounces):
    distanceTravelled += nextBounce + nextBounce*bounciness
    nextBounce *= bounciness

print("Total distance traveled is", distanceTravelled, "ft in", numberOfBounces, "bounces.")

print("Press enter to end the program.")
