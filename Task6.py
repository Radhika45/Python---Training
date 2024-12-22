#Write a program to demonstrate working with tuples in python

cars  = ("BMW", "Mercedes" , "Audi", "Range-Rover")
print("Created Tuple is: ",cars)

print("Length of Tuple: ",len(cars))

print("Type of tuple: ",type(cars))

print("All Cars: ")
for x in cars:
    print(x)

del cars

#Tuple Functions

tuple1 = (3,7,15,44,11)

print("Length: ",len(tuple1))

print("Maximum: ",max(tuple1))

print("Minimum: ",min(tuple1))

print("Sum: ",sum(tuple1))

print("Ascending Sorted tuple: ",sorted(tuple1))

print("Descending Sorted tuple: ",sorted(tuple1,reverse = True))

print("Count: ",tuple1.count(7))

print("Index: ",tuple1.index(15,1,6))

#Conversion of string to tuple
str1 = "Python"
print("String to Tuple: ",tuple(str1))
