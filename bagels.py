import random

def main():
    print("Guess the secret Number. 3 Digits")
    print("Fermi = Correct digit Correct palce/nPico = Correct Digit and wrong place/n Bagels = No Correct digits")
    print("You have 10 Tries")
    maxtries = 10
    digits = 3

    num_tries = 1
    
    while True:
    threeDigitNumber = createNumber()
    numberGuess = ' '
        #run while numtries < 10
        while num_tries < maxtries:
            num_tries+=1
            
            print("Enter a guess, it has to be {digits} digits")
            numberGuess = input("> ")
            if len(numberGuess) != digits:
                print("Your guess is not {digits} Digits long.\nPlease enter another guess")

             if numberGuess == threeDigitNumber:
                print("you guessed it! The number was {threeDigitNumber}")
                
            validNumber = isValidNumber(numberGuess) 
            print(validNumber)


            print("Number of tries: {numtries} out of {maxtries}")
            
            
    
            
    
def createNumber():
    newNumber = ''
    a = ['0','1','2','3','4','5','6','7','8','9']
    a.shuffle(a)

    for i in range(digits):
        newNumber.append(a[i])

    return newNumber 



def isValidNumber(checkNumber):
    if checknNumber == threeDigitNumber:
        print("You Got it!")


    clues = [] 
    for num in len(threeDigitNumber):
        if  numberGuess[i] == threeDigitNumber[i]:
            clues.append("Fermi")  
        if numberGuess[i] in threeDigitNumber:
            clues.append("Pico")
    else:
        clues.append("Bagels")

    return ' '.join(clues)


if __name__ == "__main__":
    main()
    

    

