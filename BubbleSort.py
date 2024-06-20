print("------Bubble Sort--------")

num= int(input("Enter Number of Elements: ")) 

ele=[]
for _ in range(num):
    element=int(input("List of Elements: "))
    ele.append(element)

print("List: ",ele)

for i in range(num):
    for j in range(0,num-i-1):
        if ele[j]>ele[j+1]:
            ele[j],ele[j+1] = ele[j+1],ele[j]

print("Elements After Sorting: ",ele)
