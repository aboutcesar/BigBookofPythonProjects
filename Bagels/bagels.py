import random

print("Guess the secret Number. 3 Digits")
print("Fermi = Correct digit Correct palce/nPico = Correct Digit and wrong place/n Bagels = No Correct digits")
print("You have 10 Tries")


threeDigitNumber = createNumber()
numberGuess = input("I have thought of a number. Enter a 3 Digit Number:")




def createNumber():
    newNumber = random.randint(100,999)

    return newNumber 

def isValidNumber(numberGuess):
    if numberGuess == threeDigitNumber:
        print("You Got it!")

    
    if len(numberGuess) < maxLength:
        print("this number is less than 3 digits long")
        continue

    clues = [] 
    for num in threeDigitNumber:
        if  == index(numberGuess):
            print("Fermi")
            continue
        if num in numberGuess:
            print("Pico")
            continue
        else:
            print("Bagels")
            continue

    

