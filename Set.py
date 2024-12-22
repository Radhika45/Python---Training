#Set Functions

set1 = { 1,2,3,4,5}
set2 = { 5,6,4,2,10}

#len, min, max, sum
print("Issubset: ",set1.issubset(set2))

print("Issuperset: ",set1.issuperset(set2))

print("Difference: ",set1.difference(set2))

print("Intersection: ",set1.intersection(set2))

print("Union: ",set1.union(set2))

print("Pop: ",set1.pop())

set1.remove(2)
print("Remove: ",set1)

set1.discard(2)
print("Discard: ",set1)

set1.clear()
print("Clear: ",set1)

set1.update("M","T","W")
print("Update: ",set1)

set1.add(23)
print("Add: ",set1)

#Conversion of String to Set
list1 = [1,2,3]
print("Conversion: ",set(list1))