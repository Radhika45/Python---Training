#List Functions
print("=======LIST========")
fruits1 = ["Apple" , "Kiwi", "Guava", "Mango"]

list1 = [2,9,4,8,10]
#1.Sort
print("Sorted: ",sorted(fruits1))

list1.sort()
print("Ascending Sort of List: ",list1)
list1.sort(reverse = True)
print("Descending Sort of lIst: ",list1)

#2.Reverse
fruits1.reverse()
print("Reverse of list1: ",fruits1)

#3.Count
list1.count(4)
print("Count 4 of list1: ",list1)

#4.Index
print(list1)
print("Index of list1:: ",list1.index(8))

#5.Insert
list1.insert(0,11)
print("Insert of list1:: ",list1)

list1.pop(2)
print("Pop: ",list1)

#Convert Anything to List
str = "Python"
print("Conversion of String to list: ",list(str))


#Tuple Functions
tuple1 = (3,7,15,45,11)
print("=========TUPLE========")

#Acscending order
print("Ascending Sorted tuple: ",sorted(tuple1))

#Descending Order
print("Descending Sorted tuple: ",sorted(tuple1,reverse = True))

#Count
print("Count tuple: ",tuple1.count(7))

#Index 
print("Index tuple: ",tuple1.index(15,1,6))

#Conversion of string to tuple
str1 = "Python"
print("String to Tuple: ",tuple(str1))


#Dictionary 
print("=======DICTIONARY=========")
student = {"Name": "Radhika", "Class": "B.Tech 3A","Roll-no": 2230080, "Domain": "CSE"}

#Get function
print("Get Specified value from key: ",student.get("Name"))

#Keys
print("Fetch all Keys: ")
for x in student.keys():
    print(x)

#items
print("Key- value Tuples: ")
for x in student.items():
    print(x)

#values
print("All Values in Dictionary: ")
for x in student.values():
    print(x)

#update
student.update({"Class": 25})
print("Update Dictionary: ",student)

#clear
student.clear()
print("Clear: ",student)

#String Functions
print("=========STRING==========")
str1 = "Python is a Programming Language"

#lower
print("Lower Alphabets: ",str1.lower())

#upper
print("Upper Alphabet: ",str1.upper())

#replace
print("Replace String: ",str1.replace("Python","Java"))

#find
print("Find : ",str1.find("y"[0:4]))

print("Index: ",str1.index("t"))

print("Isalnum: ",str1.isalnum())

print("Isdigit: ",str1.isdigit())

print("Isnumeric: ",str1.isnumeric())

print("Islower: ",str1.islower())

print("Isupper: ",str1.isupper())

#Number Functions
print("==========NUMBER==========")
a = 9
print("Int: ",type(a), a)

b= 9.18
print("Float: ",type(b),b)

c= 9+18j
print("Complex Number: ",type(c),c)

a1 = [18,45,90,9,13]
print("Length of a1 list: ",len(a1))

print("Maximum of a1 list: ",max(a1))

print("Minimum of a1 list: ",min(a1))