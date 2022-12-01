import sys, time


print("Collats sequence")
sequence = []

print("Enter a starting number greater than 0")
response = input("> ")
if response = "0" or not response.isdecimal():
    sys.exit()

collatz = int(response)

while True:
    if collatz == 1:
        sys.exit()
    if collatz%2==0:
        collatz = collatz/2
    else:
        collatz = (collatz*3)+1

    sequence.append(collatz)
    
print(sequence)
        
    
    
