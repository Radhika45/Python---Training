#Write a program to demonstrate working with dictionaries in python.

student = {'Name':'Radhika','Roll_No': 2230080 ,
           'Class': "B.Tech", 'Section' : 'A'}
print("Dictionary is :",student)

#Accessing specific values 
"""      print(<dict_name>["<key_name>"])     """
print("Student Name is: ",student['Name'])

#Display all Keys
""" for x in <dict_name>:
         print(x)         """
print("All Keys in Dictionary: ")
for x in student:
    print(x)

#Display all values
"""  for x in <dict_name>:
        print(dict_name[x])    """
print("All Values in Dictionary ")
for x in student:
    print(student[x])

#Display all keys and values
for x,y in student.items():
    print(x,y)

#Update the particular value
student["Class"] = "BCA"
print(student)

#Adding items
student["Domain"]="CSE"

#Updated dictoinary
print("Updated Dictionary is :",student)

#Dictionary Functions: 

print("Length: ",len(student))

student.pop("Class");
print("Pop using Key: ",student)

student2 = student.copy()
print("Copy Function: ",student2)

print("Get Specified value from key: ",student.get("Name"))

print("Fetch all Keys: ")
for x in student.keys():
    print(x)

print("Key- value Tuples: ")
for x in student.items():
    print(x)

print("All Values in Dictionary: ")
for x in student.values():
    print(x)

student.update({"Class": 25})
print("Update Dictionary: ",student)

student.clear()
print("Clear: ",student)