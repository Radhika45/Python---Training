"""
my_tuple =()
my_tuple = tuple()

my_list = []
my_list = list()

my_set = set()

my_dict ={}
my_dict = dict()
"""
#Built-In-Finctions in Dictionary

my_data = {
    101: "J",
    102: "R",
    103: "S",
    104: "T"
}


print("\nmy_data1: ",my_data)


print(len(my_data))
print(min(my_data))
print(max(my_data))
print(sum(my_data))

my_data2 = {
    "A": "J",
    "B": "R",
    "C": "S",
    "D": "T"
}

print("\nmy_data2: ",my_data2)


print(len(my_data2))
print(min(my_data2))
print(max(my_data2))
#print(sum(my_data2)) #Works only for int keys

my_data3 = {
    101: "J",
    102: "R",
    103: "S",
    101: "T"
}

print("my_data3 \n")
print(my_data3)


print(len(my_data3))
print(min(my_data3))
print(max(my_data3))
print(sum(my_data3))

print(my_data[101])
print(my_data.get(101))

#(1)Pop Data
my_data.pop(102)
# del my_data[102]


#(2)Appending in Dictionary
my_data[103] = "Joseph"
print("\n",my_data)


print("For printing key- months, value- constant")
attendance = ["june","july","aug","july"]
college_attendance = {}.fromkeys(attendance,100)
print(college_attendance)

items = list(my_data.items())
print("For Printing Items(Both key-value) in a List: \n",items)
values = list(my_data.values())
print("For Printing Values in a List: \n",values)


print("For Printing both Key-Value Pairs: ")
for item in my_data.items():
    print("\n",item)
    

print("For Printing all Values: ")
for value in my_data.values():
    print(value)