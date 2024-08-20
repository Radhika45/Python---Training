import datetime

def show ():
    print("This is Show")
    print("Today is: ",datetime.datetime.today())

#Refernce Copy Operation
hello = show

print("Show is: ",show)
print("Hello is: ",hello)

hello()
hello()
