#OPERATORS
'''ArithmeTic Operator -> 
 +(Addtion), -(Substraction), *(Multiplication), **(Exponentiation), /(Division), //(Floor Division), % (Modulus)'''

product_price = 200
gst_tax = 0.18

price_to_pay = gst_tax*product_price + product_price

print(price_to_pay,type(price_to_pay),id(price_to_pay))

number = 10
result = number/3   # Floating point integer
print("Result is: ",result)
result = number // 3 # // Integral Division -> we will get the complete number round off number
print("Result is: ",result)

a = 3
result = a * 2 #Multiplication
print(result)
result = a ** 2 # Exponential Power (a)^b , here 2 is power
print(result)

'''Remainder Operator -> '''
bucket_size = 7
hashcode = 120 % bucket_size #Remainder Operator -> Remainder of division 
print("Hashcode: ",hashcode)

#Assignement Operators-> =, +=, -=, *= , **=, /=, //=, %=

#A new refernence operator variable age will be created in Stack
# A container 20 will be created in heap
#Hashcode of 20 will be stored in age
#hernce age is a REFERENCE Variable
age =20

#UPDATE operation
# age = age +10
age += 10 #shorthand expression of add and assign -> 20 + 10 = 30
print("Age is: ",age)

age %= 3 # age = age % 3 -> 30 % 3 = 0
age -= 1 # age = age - 1 -> 0 - 1 = -1

print("Age now is: ",age)

#Increment and decrement
qty = 1
qty += 1 # 1+1 = 2
qty -= 1 # 2-1 = 1
qty += 5 # 1+5 = 6
qty -= 1 # 6-1 = 5
qty **=2 # (5)^2 = 25
print("Quantiy: ",qty)