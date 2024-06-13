# FUNCTIONS

#Basic For loop for executing same task again and again
'''
for idx in range (1,11):
    print(idx)

It will print numbers from 1 to 10
'''

#Using Functions for executing some task,by calling a function print_number again and again
'''
def print_number(number):
    print(number)

print_number(1)
print_number(2)
print_number(3)

It will print 1
'''

'''
#Stack-Overflow Error
def print_number(number):
    print(number)
    print_number(number+1)
#Function called infinetely and Recursion exceeded its limit

print_number(1)

'''

#Adding a Terminating Condition to the above function
def print_number(number):
    print(number)

    if number < 10:
        print_number(number+1)

print_number(1)