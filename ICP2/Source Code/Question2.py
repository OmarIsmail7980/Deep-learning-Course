

integer = int(input('Please enter an integer:'))

#function to process the input
def convert(integer):
    steps = 0
    while integer != 0:
        if(integer%2 == 0):
            integer = integer/2
        elif(integer%2 != 0):
            integer = integer-1
        steps = steps+1
        
    return steps

#run the function using the input
print("Number of steps to get to Zero: {}" .format(convert(integer)))
            
 