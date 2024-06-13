#Bitwise Opeartors -> Used to compare Binary Numbers 
'''
And -> &
Or -> |
XOR -> ^
NOT -> ~
Left Shift -> <<
Right Shift -> >>
'''
num1 = 10  # 1 0 1 0
num2 = 8   # 1 0 0 0

print("num1 in binary is: ",bin(num1)) #Binary of a Number -> 0b represents Binary
print("num1 in binary is: ",bin(num1)) 

results1 = num1 & num2 # 1 0 0 0 (In AND if Both upper and lower are true then 1, else 0)
results2 = num1 | num2 # 1 0 1 0 (In OR if either one is true , then 1 else 0)
results3 = num1 ^ num2 # 0 0 1 0 (In XOR if first is true , next should be false)

print("Result 1: ",results1)
print("Result 2: ",results2)
print("Result 3: ",results3)

#Shift Operations -> 
# >> (Right Shift), 
# << (Left Shift)

num1 = 8
num2 = 3

#                    8  >>  3  performing Right Shift
result1 = num1 >> num2 # 8 // 2 power 3
print("Result Right shift : ",result1)
number = result1 << num2
print("Number is:",number)

#                    8  <<  2  performing Left Shift
result2 = num1 << num2 # 8 * 2 power 3
print("Result Left shift ",result2)


#Arithemitic Right Shift by 2 >>

number = 13
result = number >> 2
print(number, ">> 2 is: ", result) # Result = 3
'''           How Arithemetic Right Shift Works ? -> Right Shift by 2
13 -> 0 0 0 0  1 1 0 1 

_ _ 0 0  0 0 1 1
0 0 0 0  0 0 1 1
Result = 3
'''

number = - 11
result = number >> 2
print(number,">> 2: ",result)
'''
Number = - 11
11 -> 0 0 0 0  1 0 1 1
1's   1 1 1 1  0 1 0 0
2's   1 1 1 1  0 1 0 1
      _ _ 1 1  1 1 0 1
arithemetic right shift -> add 1 in -ve number in blank space
      1 1 1 1  1 1 0 1
again 1's complement
      0 0 0 0  0 0 1 0
again 2's complement i.e add 1
      0 0 0 0  0 0 1 1 -> -3 (3 will be written as - 3 bacause number is negative i.e -11)
'''

number = -13
result = number >> 2
print(number,">> 2: ",result)

""" 
Number is - 13
       0 0 0 0  1 1 0 1
1's -> 1 1 1 1  0 0 1 0 
2's -> 1 1 1 1  0 0 1 1
       _ _ 1 1  1 1 0 0 
add 1 in space   1 1 1 1  1 1 0 0
Again 1's ->     0 0 0 0  0 0 1 1
Again 2's ->     0 0 0 0  0 1 0 0 -> 4 will be written as -4

"""

