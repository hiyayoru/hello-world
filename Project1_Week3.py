grossIncome = float(input("Please input gross income: "))
dependents = float(input("Please input number of dependents: "))

taxableIncome = grossIncome - 10000 - 3000 * dependents

Tax = taxableIncome * 0.20

print("Total tax owed: ", round(Tax, 2))

input("Press enter to exit: ")
