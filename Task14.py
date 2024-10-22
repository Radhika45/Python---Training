'''Write a python program to define a module to find Fibonacci Numbers and import the
module to another program'''

# file-name = fibonacci.py , function-name = fib
"""  
1. Create a required function in one file and name it as same file-name you want to import.
2. In another file import the previous file and call that function name as  file-name.function-name(variable)"""
#import fibonacci module
import fibonacci
num=int(input("Enter any number to print Fibonacci series: "))
fibonacci.fib(num)
