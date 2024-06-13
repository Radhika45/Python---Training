#Calling Functions in Memory

def square(num):
    print("1.num is: ",num,id(num)) #10
    num *= num #100
    print("2.num is:",num) #100
    # return 

#Function exists in memory
#print("square:",square) -> hashcode and name of function in memory
number = 10
print("A.Number is: ",number,id(number)) #10
square(number)
print("B.Number is: ",number,id(number)) #10

# A will be printed first because A is called at first , after that "square" function is called.