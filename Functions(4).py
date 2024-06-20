#FUNCTIONS
#Creaing Add Function
def add(num1, num2):
    result = num1 +num2
    print("Result 1 is: {}".format(result))

#Printing Hex Code of Add
print(hex(id(add)))
print("Add is: ",add)

#Executing Add Function
add(10, 20)

#Refernce Copy Operation
hello = add #Whatever we write in "Add" function will be executed using values of "Hello"

#Executing Hello Function
hello(11,22)

#If we redifine the same "Add" function , previous function will be deleted.
def add(num1,num2,num3):
    result=num1 +num2 +num3 +10
    print("Result 2: ",result)

#Now,this ADD function will have another hashcode
print(hex(id(add)))
print("Add is: ",add)

add(10,20,30)