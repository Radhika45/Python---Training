#List Functions
fruits1 = ["Apple", "Guava"]
print("Length: ",len(fruits1))

print("Max: ",max(fruits1))

print("Min: ",min(fruits1))

list1 = [1,2,3,9,9]
print("Sum: ",sum(list1))

print("Sorted: ",sorted(fruits1))

list1.sort()
print("Ascending Sort: ",list1)
list1.sort(reverse = True)
print("Descending Sort: ",list1)

#Convert Anything to List
str = "Python"
print("Conversion of String to list: ",list(str))

fruits1.reverse()
print("Reverse : ",fruits1)

list1.count(4)
print("Count 4: ",list1)

print(list1)
print("Index : ",list1.index(8))

list1.insert(0,11)
print("Insert: ",list1)

list1.pop(2)
print("Pop: ",list1)

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


student ={
    "Name": "Radhika",
    "Class": "12th"
}
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

print("Length: ",len(str1))

print("Lower Alphabets: ",str1.lower())

print("Upper Alphabet: ",str1.upper())

print("Replace String: ",str1.replace("Python","Java"))

str2 = "Python"
str3 = str1.join(str2)
print("Join String: ",str3)

print("Find : ",str1.find("y"[0:4]))

print("Index: ",str1.index("t"))

print("Isalnum: ",str1.isalnum())

print("Isdigit: ",str1.isdigit())

print("Isnumeric: ",str1.isnumeric())

print("Islower: ",str1.islower())

print("Isupper: ",str1.isupper())