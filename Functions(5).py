def add(num1,num2,num3):
    result = num1 + num2 +num3
    print("Result 1 is: {}".format(result))

#add(10,20,30) or add(num1 = 10,num2 =20,num3=30) are same
add(num1 = 10,num2 =20,num3=30)

#Default Arguments/Inputs
def square(num=5):
    result = num * num
    print("Result 2 is: {}".format(result))

square() #It will use Default value i.e num=5
square(3)
square(num=9)

#def substract(num1= 10, num2)->Will give error as we cannot assign default value for num1
def substract(num1,num2 = 5): 
    result=num1 -num2
    print("Result 3 is: {}".format(result))

substract(num1=15)