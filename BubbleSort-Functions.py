#Bubble Sort using Functions
def bubble_sort(data):
    for i in range(len(data)-1):
        print("i is: ",i)
        for j in range(len(data)-i-1):
            print(j,end=" ")

            if data[j]>data[j+1]:
                print("Swapping  {} with {} ".format(data[j],data[j+1]))
                data[j],data[j+1] = data[j+1],data[j]
           
        print()

numbers = [10,30,50,20,40]

print("Unsorted Numbers: ")
print(numbers)
print("------------------")
bubble_sort(numbers)
print("Sorted Numbers: ")
print(numbers)
