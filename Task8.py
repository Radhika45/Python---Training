# Write a python program to find largest of three numbers

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if (num1 >= num2) and (num1 >= num3):
    print("The Largest Number: ",num1)

elif (num2 >= num1) and (num2 >= num3):
    print("The Largest Number: ",num2)

else:
    print("The Largest Number: ",num3)