import random

print("Guess the secret Number. 3 Digits")
print("Fermi = Correct digit Correct palce/nPico = Correct Digit and wrong place/n Bagels = No Correct digits")
print("You have 10 Tries")

def main():
    maxtries = 10
    digits = 3

    num_tries = 1
    #run while numtries < 10
    while True:
    threeDigitNumber = createNumber()
    numberGuess = ' '

        while num_tries < maxtries:
    
            print("Enter a guess, it has to be {digits} digits")
            numberGuess = input("> ")

            if len(numberGuess) != digits:
                print("Your guess is not {digits} Digits long.\nPlease enter another guess")

            
            if numberGuess == threeDigitNumber:
                print("you guessed it! The number was {threeDigitNumber}")
        
    
    
    
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
    for num in range(threeDigitNumber):
        if  numberGuess[i] == threeDigitNumber[i]:
            clues.append("Fermi")  
        if numberGuess[i] in threeDigitNumber:
            clues.append("Pico")
    else:
        clues.append("Bagels")

    return ' '.join(clues)


    

    

