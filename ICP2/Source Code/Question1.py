
#number of inputs
numOfElements = int(input("Enter number of elements:"))

output = []
students = []

#populate the list
for i in range(numOfElements):
    x = float(input( "Enter height in feet:"))
    
    students.append(float(x))    

#convert from ft to cm
def convert(students):
    for i in students:
        i = i*30.48
        
        output.append(i)
        
        
    return output

#call convert
print("\nheight converted to cm:" ,convert(students))
