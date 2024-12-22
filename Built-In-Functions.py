num = 4.5
print("Round off: ",round(num))

print("Absolute: ",abs(num))

x = bool(1)
print(x)

print('(8, 4) = ', divmod(8, 4))

list1 = [10,5,7]
print("All Function: ",all(list1))

list2 = [True, True, False]
print("All Function: ",all(list2))


def map_function(n):
    return n + n

numbers = (1,2,3,4)
result = (map(map_function, numbers))
print("Map Function: ",list(result))

number1 = [3,4,5,6]
result1 = map(lambda x: x+x, number1)
print("Lambda Function: ",list(result1))
