#COMPARISON OPERATORS
# == (equal to), != (not equal to), >(greater than), <(less than), <=(less than or equal to) , >= (greater than or equal to)

cab_fare = 500
e_wallet = 200

result = e_wallet >= cab_fare
print("Can I Book the Cab: ",result) #prints true or false
print(type(result))


#LOGICAL OPERATORS -> and , or ,not  -> same as DE

'''Email Authetication'''

email = input("Enter Email: ")
password = input("Enter Password: ")
#and
print("Is Login Success ?")
result = (email == "ram@gmail.com") and (password == "ram1")
print(result)

otp = 234
user_otp = int (input("Enter OTP received: "))
print("Is OTP correct", otp==user_otp)

#Membership Testing -> is , is not
a = 10
b = 10

print(a == b) # prints True if a is equal to b
print(a is b) # prints True if a is equal to b , else False
print(a is not b) # prints True if a is not equal to b , else False

