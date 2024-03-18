import random

rList = random.sample(range(100), 100)
list = [1, 2, 3, 4]
string = "Hello world!"
tuple = (48,84,42)

def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])

print("Testing list:", list) 
printAll(list)

print("Testing string: ", string)
printAll(string)

print("Testing tuple: ", tuple)
printAll(tuple)

print("Testing random list:")
printAll(rList)
