#Reference Copy Operation

#Using Numbers

numbers_1 = [2,4,6,8,10,12]
print(numbers_1,type(numbers_1),id(numbers_1))

#RCO using numbers -> It copy HashCode
numbers_2 = numbers_1
print(numbers_2,type(numbers_2),id(numbers_2))

print (id(numbers_1[3]))

#Changing Values of Numbers
numbers_1[3]= 30
print(id(numbers_1[3]))
print(id(numbers_2[3]))



