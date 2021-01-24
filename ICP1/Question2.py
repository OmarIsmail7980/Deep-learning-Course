
# PART 1
p = input("welcome, please enter a string:")

# remove 2 characters of the string
result = p[:-2]

#print the reversed string
print("The result is: ",result[::-1])




# PART 2
num1 = input ("Please enter a number:")
num2 = input("Please enter a number:")


firstNum = int(num1)
secondNum = int(num2)


print('\n',"The resulted Addition: {}" .format(firstNum + secondNum),'\n')
print(" The resulted Subtraction: {}" .format(firstNum - secondNum),'\n')
print(" The resulted Multiplication: {}" .format(firstNum * secondNum),'\n')
print(" The resulted Division: {}" .format(firstNum / secondNum),'\n')