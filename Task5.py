#Write a program to create, append, and remove lists in python.

#List Creation
fruits1 = ["Apple", "Mango", "Guava", "Pear"]
print("Fruits are: ",fruits1)
Vegetables1 = ["Potato", "Tomato", "Brinjal"]
print("Vegetables are: ",Vegetables1)
list1 = [ 4 , 7, 8, 2]

#Append Function
fruits1.append("Banana")
print(fruits1)
print("Fruits: ",fruits1.append("Kiwi"))

Vegetables1.append("Pumpkin")
print(Vegetables1)

#Remove List
fruits1.remove("Apple")
print("After from Removing List:",fruits1)

list1.remove(7)
print("List1: ",list1)

#List Functions
print("Length: ",len(fruits1))

print("Max: ",max(fruits1))

print("Min: ",min(fruits1))

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

list1.clear()
print("Clear: ",list1)