startingSalary = float(input("Please enter your starting salary: "))

yearlyIncrease = int(input("Please enter your yearly percentage increase: "))

numberOfYears = int(input("Please enter how many years you have worked here: "))

maxYears = 10

yearlyIncrease /= 100
yearlyIncrease += 1

print("%-4s%9s" % ("Year", "Salary"))
for i in range(1, numberOfYears+1):
    print("%-6d$ %6.2f" % (i, startingSalary))

    if(i <= maxYears):
        startingSalary *= yearlyIncrease
