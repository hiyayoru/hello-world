iterationCount = int(input("Please enter the number of iterations you would like to calculate: "))

approximateValue = 0

sign = 1

for i in range(1, iterationCount*2+1, 2):
    approximateValue += 1 / (sign * i)
    sign *= -1

print("The approximate value of pi after", iterationCount, "iterations is", approximateValue*4)
