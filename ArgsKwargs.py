# When you need to pass variable input to function (i.e 1 number or n numbers)
#*args function to pass variable arguments inuts to the code

print("=============Args=========")
def add(*args):
    print(args)
    print(type(args))
    data = list(args) #To convert tuple in the form of list
    print(data)
    print(type(data))

add( 10, 20, 30, 40, 50, 60, "hi", "hello")
print()

#** Dictionary key - value arguments
print("==========KWARGS============")
def numbers(**kwargs): 
    print(kwargs)
    print(type(kwargs))

numbers ( a = 10, b = 20 , c=30)
print()

def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(10,20,30,40,50,"hi",'john',a= 10, b= 20 ,c=40)
