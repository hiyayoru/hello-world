import shutil
import sys

# File copy loop
while True:
    print("You can input the the file path if you are copying files between directories.") # statement that lets the user know they can copy between directories if they use the file path

    # Asks the user to input the file they want to copy and where it should copy that file to
    copyFile = input("Pleae enter the name of the file you want to copy: ") 

    destinationFile = input("Please enter the name of the destination file you want to copy to: ")

    shutil.copyfile(copyFile, destinationFile)

    print("The copied file has been copied over to the destination file.")

    # Determines whether the user wants to continue to copy files or not
    question = input("Would you like to transfer more files? (yes or no): ")
    if question.lower() != 'yes':
        print("Thank you for using this program.")
        sys.exit()

