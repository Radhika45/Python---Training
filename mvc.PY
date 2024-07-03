# When you need to pass variable input to function (i.e 1 number or n numbers)
#*args function to pass variable arguments inuts to the code


def add(*args):
    print(args)
    data = list(args) #To convert tuple in the form of list
    print(type(args))
    print(type(data))

add(10,20,30,40,50,60,"hi","hello")

def numbers(**kwargs): #** Dictionary key - value arguments
    print(kwargs)
    print(type(kwargs))

numbers ( a = 10, b = 20 , c=30)

def fun(*args,**kwargs):
    print(args)
    print(kwargs)

fun(10,20,30,40,50,"hi",'john',a= 10, b= 20 ,c=40)
