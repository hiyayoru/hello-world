import sys

# While loop to encrypt a message with a caesar cipher
while True:
    
    plainText = input("Enter a one-word, lowercase message: ")
    distance = int(input("Enter the distance value: "))
    code = ""

    # Caesar Cipher 'calculation'
    for ch in plainText:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                          (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
    print(code)

    # Question and if statement that determines whether the user wants to encrypt a new message or not
    question = input("Would you like to encrypt a new message? (yes or no)") 
    if question.lower() != 'yes':
        print("Thank you for using this program.")
        sys.exit()
