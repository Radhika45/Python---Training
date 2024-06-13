#Finding maximum Using Recursion

#Program for finding Max using For Loop
'''
numbers =[1,3,5]

max = numbers[0]

for idx in range (1,len(numbers)):
    if numbers[idx] > max:
        max = numbers[idx]

print("Max is: ",max)
'''

#Using Recursion other than for Loop: For finding Maximum Value
#(a)- If one number is given in a List
'''
def get_max(data, length):

    if length == 1:
        return  data[0]
       
numbers = [10]

result = get_max(numbers,len(numbers))
'''

#(b)- If two numbers are given using If-Else Loop
'''
def get_max(data, length):

    if len(data)  == 1:
        return data[0]
    else: 
        len(data) == 2
        if data[0]<data[1]:
            return data[1]
        else:
            data[0]>data[1]
            return data[0]
    
numbers = [10,20]

max = get_max(numbers, len(numbers))
print("Max is: ",max)
'''

#(c)Approach Using Recursion
def get_max(data, length):

    if length  == 1:
        return data[0]
    else: 
        previous = get_max(data,length-1)
        current = data[length-1]

        if previous > current:
            return previous
        else:
            return current
    
numbers = [1,5,3]

max = get_max(numbers, len(numbers))
print("Max is: ",max)
    