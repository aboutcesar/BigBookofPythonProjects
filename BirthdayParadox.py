import datetime
import sys
import random



bdaylist = []
numtrials = 100000


def main():

    while True:
            
        amount = input("Enter the number of Birthdays that you want to displayed (MAX 100)")
        if amount.isdecimal() and (0 > amount <100):
            numdays = int(amount)
            break
        print()

    
    bdaylist = birthdayList(amount)
    displayBirthdays(bdaylist)
    matches = foundmatch(bdaylist)
    print("In this simulation the following birthdays were repeated")

    print(matches)
    probability = runsimulation(numtrials,amount)
    
    print("the probability of {amount} having matching birthdays is {probability}%")
    
    
    

    
def generate_birthday():
    timestart = datetime.datetime(2021,1,1,0,0,0,0,0)
    endime    = datetime.datetime(2021,12,31,0,0,0,0,0)

    randomday = random.ranint(0,364)
    birthday = timestart + randomday
    
    return birthday

def birthdayList(numberofBirthdays):
    bdaylist = [generate_birthday() for x in range(0,numberofBirthdays)]
    return bdaylist


def displayBirthdays(bdaylist):
    print("Here are the birthdays")
    for x in range(bdaylist):
        print(bdaylist[x])
    print()

    
def foundmatch(bdaylist):
    repeats = []
    if len(bdaylist) == len(set(bdaylist)):
        return None
    else:
        for number, date1 in enumerate(bdaylist):
              for number, date2 in enumerate(bdaylist):
                  repeats.append(date1)
    return repeats
              

def runsimulation(numtrials, amount):
    num_matches = 0
    for x in range(numtrials):
        list_bday = birthdayList(amount)
        ismatch = foundmatch(list_bday)

        if ismatch:
            num_matches +=1

    probability = round(num_matches/100000*100,2)
    return probability     
    
        
                  
    



def __init__ == "__main__":
    main()
            

        
