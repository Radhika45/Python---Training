#Write a program to demonstrate working with dictionaries in python.

student = {'Name':'Radhika','Roll_No': 2230080 ,
           'Class': "B.Tech", 'Section' : 'A'}
print("Dictionary is :",student)

#Accessing specific values 
print("Student Name is: ",student['Name'])

#Display all Keys
print("All Keys in Dictionary: ")
for x in student:
    print(x)

#Display all values
print("All Values in Dictionary ")
for x in student:
    print(student[x])

#Adding items
student["Domain"]="CSE"

#Updated dictoinary
print("Updated Dictionary is :",student)

#Removing Items
student.pop("Class");
#Updated dictoinary
print("Updated Dictionary is :",student)

#Length of Dictionary
print("Length of Dictionary is :",len(student))

#empties the dictionary
student.clear()
print("Updated Dictionary is :",student)