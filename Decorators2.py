
#Function as Input
#i.e Passing the function by Reference
def show (func):
    print("Show Executed")
    func()

def hello():
    print("This is Hello")
    print("Hello Function Finished....")

def bye():
    print("This is Bye")
    print("bye function finished")

show(hello)
print("``````````````````````")
show(bye)