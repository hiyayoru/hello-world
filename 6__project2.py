import sys

# While loop to decrypt a caeser cipher message
while True: 
    code = input("Enter the encrypted text: ")
    distance = int(input("Enter the distance value: "))
    plainText = ''

    # Caesar Cipher decryption calculation
    for ch in code:
        ordvalue = ord(ch)
        cipherValue = ordvalue - distance
        if cipherValue < ord('a'):
            cipherValue = ord('z') - \
                                      (distance -(ord('a') - 1))
        plainText += chr(cipherValue)
    print("Decrypted message is: ", plainText)

    # Question and if statement that determines whether the user wants to decrypt a new message or not
    question = input("Would you like to decrypt a new message? (yes or no)") 
    if question.lower() != 'yes':
        print("Thank you for using this program.")
        sys.exit()
