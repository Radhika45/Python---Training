#Write a python program to find factorial of a number using Recursion.

def factorial(n):
    if n==0 or n==1:
        return 1
    
    else:
        return (factorial(n-1)*n)
    
number = int(input("Enter Number to find Factorial: "))
if number < 0:
    print("Factorial for Negative Number is not Possible")

else:
    print("Factorial of ",number ,"is", factorial(number))