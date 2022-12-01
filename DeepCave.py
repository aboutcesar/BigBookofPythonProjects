import sys, time, random



total_width = 65 
timepause = .5  #seconds pause

leftwidth = 15
rightwidth = 35
gapwidth = 15
print("Deep Cave")
print("Press Ctr+C to stop")

while True:
    #print initial starting point
    print("*"*leftwidth+' '*gapwidth+"*"*rightwidth)
    #sleep and see if there is an interruption
    try:
        time.sleep(timepause)
    except keyboardInterrupt:
        print("Run Finished.")

    
    changegap = random.randint(1,4) #1 decreases and 3 increases the left width 

    if changegap == 1 and leftwidth >1:
        leftwidth -= changegap
        rightwidth = rightwidth - gapwidth - leftwidth)
    elif changegap == 3 and leftwidth + width < rightwidth-1:
        leftwidth += 1
        rightwidth = rightwidth - gapwidth - leftwidth)
    else:
        pass 
