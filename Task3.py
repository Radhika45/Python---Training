#Write a program to create, concatenate and print a string and accessing sub-string from a given string

#Giving Self Input
str1 = "Python"
print("String1: ",str1)

#Taking Input from User
str2 = input("Enter Any String: ")

#Concatenation of two strings
print(str1 + " ",str2)

#Sub-String of a given String
print("Sub-String of a String",str1[1:4])

#String Functions
print("Length: ",len(str1))

print("Lower Alphabets: ",str1.lower())

print("Upper Alphabet: ",str1.upper())

print("Replace String: ",str1.replace("Python","Java"))

str3 = str1.join(str2)
print("Join String: ",str3)

print("Find : ",str1.find("y"[0:4]))

print("Index: ",str1.index("t"))

print("Isalnum: ",str1.isalnum())

print("Isdigit: ",str1.isdigit())

print("Isnumeric: ",str1.isnumeric())

print("Islower: ",str1.islower())

print("Isupper: ",str1.isupper())