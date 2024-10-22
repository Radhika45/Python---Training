'''Write a python program to define a module and import a specific function in that
module to another program.'''
# file-name = arth.py, function-name - Add

from arth import Add 
num1=float(input("Enter first Number : "))
num2=float(input("Enter second Number : "))
print("Addition is : ",Add(num1,num2))
print("Subtraction is : ",Sub(num1,num2)) #gives error:Not importing Sub function from arth Module