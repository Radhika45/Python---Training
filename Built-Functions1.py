# LIST 
# List can be appended and numbers can be added
print("=======LIST======")
""" variable_name = list(range(starting_limit, end_limit, gap_limit))"""
numbers = list(range(10,101,10))
print("Numbers is: ",numbers)
print("Numbers Type is: ",type(numbers))

#(1)Appending - Adding numbers in the end of the List
""" variable_name.append(new_number)"""
numbers.append(99) 
numbers.append(77)
numbers.append(103)
numbers.append(11)

#(2)Built-In-Functions 
""" len(variable_name)  , sum(variable_name), min(varaible_name) ,
 max(variable_name)"""

print("Numbers is: ",numbers)
print("Len is: ",len(numbers))
print("Sum is: ",sum(numbers))
print("Min is: ",min(numbers))
print("Max is: ",max(numbers))
print("Average is: ",sum(numbers)/len(numbers))

#(3)Reversing the List
""" variable_name2 = list(reversed(variable_name1))"""
result = list(reversed(numbers))
print("Result is: ",result)
print()

#TUPLE
#(1)Tuple cannot be appended
print("======TUPLE=======")
numbers = tuple(range(10,101,10))
print("Numbers is: ",numbers)
print("Numbers Type is: ",type(numbers))

#(2)Built-In-Functions 
""" len(variable_name)  , sum(variable_name), min(varaible_name) ,
 max(variable_name)"""
print("Numbers is: ",numbers)
print("Len is: ",len(numbers))
print("Sum is: ",sum(numbers))
print("Min is: ",min(numbers))
print("Max is: ",max(numbers))
print("Average is: ",sum(numbers)/len(numbers))


# Different Methods for printing Index of numbers
data = [10,20,30,40,50,30]
"""
#  0 1 2 3 4
1. Using For Loop
data1 = []

for idx in range(len(data)-1, -1 , -1):
    print(data[idx])
    data1.append(data[idx])

print(data1)
"""

#(2)Using index Function
""" variable_name = list_name.index(idx_of_number)"""
idx = data.index(40)
print("idx is : ",idx)

#(3)Using count Function
""" variable_name = list_name.count(idx_of_number)"""
result = data.count(30)
print("Result is: ",result)

#(2)Using For loop 
c = 0
for idx in range(len(data)):
    if data[idx] == 30:
        c+=1
print("c is: ",c)

data = [10,20,30,40,50,5,19]
names = ["john","jennie","sia","kim"]

#(4)Sort(),(5) Min() ,(6) Max() built in Function works on Homogeneous data only
data.sort()
print("Data is: ",data) #sort data in ascending order
names.sort()
print("Names: ",names)  #sort names according to unicode

print("Minimum Name: ",min(names))
print("Maximum Name: ",max(names))
#Sum() does not work on Names
#print(sum(names)) 

#(7) Remove function
""" Variable_name.remove(name_of_element)"""
names.remove("sia")
data.remove(30)

print("Data is: ",data)
print("Names is: ",names)

#(8) pop() opearation
""" variable_name.pop(idx_of_number)"""
data = [10,20,30,40,50]
data.pop()
data.pop(0)
data.clear() #Every Element from the list would be deleted
print("Data after Pop: ",data)

data = [10,20,30,40,50]
data.append(99)
#(9)Insert operation
""" list_name.insert(idx_at_which_ele_should_be_added, ele)"""
data.insert(2,77)  # Insert 77 at 2nd Index 
""" Insert cannot insert any element at end it will perform -1 than last. Append is the only way to perform insertion at end"""
print("Data is: ",data)
