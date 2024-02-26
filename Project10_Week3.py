hourlyWage = float(input("Please enter hourly wage: "))

regularHours = float(input("Please enter the regular amount of hours worked this week (do not include overtime): "))

overTimeHours = float(input("How many overtime hours did you work (enter 0 for none): "))

regularPay = hourlyWage * regularHours

overTimePay = overTimeHours * (hourlyWage * 1.5)

weeklyPay = regularPay + overTimePay

print("Total pay for the week is: $",weeklyPay)
    
input("Press enter to close")
