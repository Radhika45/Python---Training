#Calling Functions in List

def square_of_numbers(num):
    print("1.num is: ",num,id(num))
    
    for idx in range(0,len(num)):
        num[idx] =num[idx] * num[idx]
    print("2.num is:",num,id(num))
    print(" ")

#print("square:",square) -> hashcode in memory
number = [10,20,30,40]
print("A. number is",number, id(number))
print("A.numbers[0] hashcode: ",id(number[0]))

print(" ")
#calling above created function now
square_of_numbers(number)
print("B.number is:",number, id(number))
print("B.numbers[0] hashcode: ",id(number[0]))

