"""
Multi Value Container

Sequences:
         1) Tuple ()
         2) List  []
         3) String ""

         4) Set {}
         5) Dictionary {key-value pair}

Properties:
         1) Indexing
         2) Negative Indexing
         3) Slicing
         4) Concatenation
         5) Multiplicity
         6) Memebership Testing
"""



#1)INDEXING (+ve and -ve)

print("=======INDEXING=======")
"""
1D LIST 
+ve =      0, 1, 2                   
-ve =     -3,-2,-1  
len =      1, 2, 3    """

my_data = [10,20,30]

print(my_data[0])  # 0th Index will print = 10
print(my_data[-1]) # -1th Index will print = 30
print(len(my_data))# length = 3
print()

"""
2D LIST (List of Lists) """
numbers = [          # +ve(top to bottom), -ve(bottom to top)
       [10,20,30],   # 0                 , -3
       [30,40,50],   # 1                 , -2
       [60,70,80]    # 2                 , -1
]

print(numbers[0])   # 0th Index will print [10,20,30]
print(numbers[-1])  #-1th Index will print [60,70,80]
print(len(numbers)) # Length = 3
print()

"""
3D(List of List of Lists)"""
large_data = [
         [ [10,20,30],  #0 , -3                0        -2
           [30,40,50],  #1,  -2
           [60,70,80]   #2,  -1
         ] ,

         [
             [140,200,30],    # 0,  -3          1        -1
             [30,40,50,60,70],# 1,  -2
             [60,70]          # 2   -1
         ],
]

print(large_data[0])        #To print [ [10,20,30], [30,40,50], [60,70,80]]
print(large_data[-1])       #To print [ [140,200,30], [30,40,50,60,70], [60,70]]
print(len(large_data))      #To print length of Data
print()


print(large_data[1][0][0]) #To print 140 i.e [1] for second List , [0] for first row , [0] for first element
print(large_data[-1][-3][-3]) #To print 140 using negative Indexing

name = "Johns Cafe"
name= "John\'s Cafe"
name= """JohnCafe
Welcome to Cafeteria
Today 's Menu:
Burger
Coffee
Pizza"""

print(name)
print(name[0]) #J
print(name[-1]) #a
print(name[-2]) #z
print(len(name))
print()

#2)SLICING
print("=====SLICING======")
""" 
+ve =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
-ve = -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
List= [10,20,30,40,50,60,70,80,90,100]"""

data = list(range(10,101,10))  #Start from 10 upto 101(1 less than 101)i.e 100 in gap of 10
print("Data is: ")
print(data)

print("Data[0:3] ", data[0:3])
print("Data[3:7] ",data[3:7])
print("Data[5:] ",data[5:])   # 5 to n
print("Data[:4] ",data[:4])   # 0 to 4

print("Data is [-5:] ",data[-5:]) # -5 to -1
print("Data is [:-4] ",data[:-4]) # -n to -4
print("Data is [-5:-2]",data[-5:-2])
print()

email = "john@example.com"
print("email[-4:]: ",email[-4:])
print("email[12:]: ",email[12:])
print()

#4)CONCATENATION
print("========CONCATENATION=======")
data1 = [10,20,30]
data2 = [40,50,60]
data3 = data1 +data2
print("Data 3 = Data1 + Data2", data3)
print()

#4)MULTIPLICITY
print("=======MULTIPLICITY=========")
data4 = data1 *2
print(data4)
print()

#5)MEMBERSHIP TESTING -> Short cut for Else ,if
print("==========MEMBERSHIP TESTING===========")
prices =[100,200,300]
prices1 =prices *2
 
print(10 in prices)   
print(100 not in prices)
print()
"""      0123456   """
quote = "Search the candle"
print(quote[6])             #6 will give space and print nothing



