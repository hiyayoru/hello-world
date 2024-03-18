import sys

# Employee Wage Report loop
while True:
    employeeInfo = input("Please enter the name of the file that contains all the employees information: ") 

    info = open(employeeInfo, 'r') # Assigned the open statement to 'file' in order to make it easier to open the file later on

    # Checks if the file was opened correctly
    if info:
        print("Employee Wage Report: ")
        print("{:<20} {:<20} {:<15} {:<15}".format("Last Name", "Hourly Wage", "Hours Worked", "Wages Paid")) # Report format
        print("-" * 70) # Added hyphens under to seperate the header from the employees

        # Splitting the line into different subjects
        for line in info:
            last_name, hourly_wage_str, hours_worked_str = line.split()
            hourly_wage = float(hourly_wage_str)
            hours_worked = float(hours_worked_str)

            # Wage calculation
            wages_paid = hourly_wage * hours_worked

            # Printed employee format
            print("{:<20} ${:<19.2f} {:<15.2f} ${:<15.2f}".format(last_name, hourly_wage, hours_worked, wages_paid))
            print("-" * 70) # Added hyphens below each employee in order to increase readability
        info.close()

    # Asks whether the user wants to calculate a new report or not
    loopQuestion = input("Would you like to calculate a new report? (yes or no)")
    if loopQuestion.lower() != 'yes':
        print("Thank you for using this program.")
        sys.exit()


    
