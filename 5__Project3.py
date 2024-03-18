# Initial input and necessary calculations
purchasePrice = float(input("Enter the purchase price: "))
downPayment = purchasePrice * 0.10
balance = purchasePrice - downPayment
annualInterestRate = 0.12
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = (purchasePrice * 0.05)
monthNumber = 0

# Table code and caclulations 
print("Month\tTotal Balance\tInterest Owed\tPrincipal Owed\tPayment\t\tRemaining Balance")
while balance > 0:
    monthNumber += 1
    interest = balance * monthlyInterestRate
    principal = monthlyPayment - interest
    remainingBalance = balance - principal
    if remainingBalance < 0:
        remainingBalance = 0
        principal = balance
        monthlyPayment = principal + interest
    print(f"{monthNumber}\t{balance:.2f}\t\t{interest:.2f}\t\t{principal:.2f}\t\t{monthlyPayment:.2f}\t\t{remainingBalance:.2f}")
    balance = remainingBalance
