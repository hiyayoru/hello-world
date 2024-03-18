import sys
# Right triangle question loop
while True:
    # Questions to determine the sides of the triangle
    hypotenuse = float(input("Enter the length of the hypotenuse: "))
    base = float(input("Enter the length of the base: "))
    perpendicular = float(input("Enter the length of the perpendicular: "))

    # If and Else statement to determine whether the trangle is a right one or not
    if base**2 + perpendicular**2 == hypotenuse**2:
        print("This is a right triangle.")
    else:
        print("This is NOT a right triangle.")

    # Question to determine if the user wants to continue to use the program or not
    question = input("Enter 'yes' to input new numbers or enter 'exit' to leave the program: ")
    if question == 'exit':
        print("Thank you for using this program.")
        sys.exit()
    else:
        question = input("Enter 'yes' to input new numbers or enter 'exit' to leave the program: ")
              
