#REFERENCE COPY OPERATION
                                  #Using Strings
#Create Statement
discount_voucher1 = "BEST20"
print(discount_voucher1,type(discount_voucher1),id(discount_voucher1))

#Reference Copy Operation
discount_voucher2 = discount_voucher1 #both the variables will have same id 
print(discount_voucher2,type(discount_voucher2),id(discount_voucher2))

#Delete
del discount_voucher1                 #There will be no effect on printing second variable, no matter if variable 1 has been deleted as its value has been stored in second variable.
print(discount_voucher2,type(discount_voucher2),id(discount_voucher2))

# It will produce Error as Var1 has been deleted
print(discount_voucher1,type(discount_voucher1),id(discount_voucher1))


                                

