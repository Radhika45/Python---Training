#Properties wont'be working on Set and Dictionary

#SET
print("---------------------------SET------------------------------")


#1)Indexing
print("=====INDEXING=====")
"""Fruits = {"Apple","Banana","Mango","Guava"}
print(Fruits[0])
"""
print("Indexing does not work on SET")
print()


#2)Slicing on Set
print("=====SLICING=====")
"""
data = set(range(10,101,10))
print(data[:2])
"""
print("Slicing does not work on SET")
print()

#3)Concatenation
print("=====Concatenation=====")
"""
data1 = {10,20,30}
data2 = {40,50,60}
data3 = data1 +data2
print("Data 3 = Data1 +Data2", data3)
"""
print("Concatenation does not work on SET")
print()


#4)MemberShip Testing -> Short cut for Else ,if
print("=====MemberShip Testing=====")
prices ={100,200,300}
#prices1 =prices *2
 
print(10 in prices)   
print(100 not in prices)
print("MemberShip Testing does work on SET")
print()


#Dictionary
print("------------------------Dictionary---------------------")

Fruits = {
    1:"Apple",
    2:"Banana",
    3:"Mango",
    4:"Papaya"
}

print("Fruits",Fruits)

#1)Indexing on Dictionary
print("=====INDEXING=====")
print(Fruits[1])
print("Indexing does work on Dictionary")
print()

#2)MEMBERSHIP TESTING 
print("===========MEMBERSHIP TESTING========")
print(1 in Fruits)
print("Papaya" in Fruits)
print("Membership Testing work in Dictionary")

