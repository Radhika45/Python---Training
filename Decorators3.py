#Nested Functions
#create function inside the other function

#Method 1 to Implement Inner Function 
def outer():
    print("This is outer Function")

    def inner():
        print("This is Inner function")
    #Inner Function will only run inside the outer function,not anyehere else
    inner()

outer()

#Method 2 To implement inner Function
def outer():
    print("This is outer Function")
    
    def inner():
        print("This is Inner function")
        print("Hashcode of Inner: ",inner)
    #Inner Function and Result will have same Hashcode
    return inner
     
result = outer()
print("Hashcode of Result: ",result)
result()


