""" Object Oriented Programming  """

#Principle of OOPS:
"""1.Think of an Object"""

#FlightBooking: fromLocation , toLocation , travelDate, numberofTravellers, travelClass

"""2.Create class of Object
Below class represents the object.It is a description of object.
"""
class FlightBooking:
    pass

"""3.Create the Real Object from class in Memory
Below is Object construction Statement """

booking1 = FlightBooking()
#booking1 is a Reference Variable, FlightBooking() - Represents the Object Construction

print(booking1)
print(vars(booking1))

print(id(booking1))
print(hex(id(booking1)))

booking2 = FlightBooking()

#Reference Copy Operation
booking3 = booking1

#OPERATIONS ON OBJECT
#1.Write Operation

booking1.fromLocation = "Ludhiana"
booking1.toLocation = "New Delhi"
booking1.travelData = "18 June 2024"
booking1.numberofTravellers = 1
booking1.travelClass = "Premium"
booking1.bookedat = "9:00 27 May 2024"

booking2.fromLocation = "New Delhi"
booking2.toLocation = "Bengaluru"
booking2.travelData = "18 June 2024"
booking2.numberofTravellers = 3
booking2.travelClass = "Business"
booking2.bookedat = "9:00 27 May 2024"

#2.Update Operation

booking3.numberofTravellers = 4
booking3.travelClass = "Premium Economy"

#4.Read Operation
print("Booking1 data: ")
print("FROM: ",booking1.fromLocation,"TO: ",booking1.toLocation) #To print specific Attributes
print(vars(booking1)) #To print all Attributes of Booking1

print("Booking2 Data: ")
print("FROM: ",booking2.fromLocation,"TO: ",booking2.toLocation) #To print specific Attributes
print(vars(booking2)) #To print all Attributes of Booking2

#5.Delete Operation

#(a) To Delete any Specific Attribute
del booking1.travelClass
print("Booking1 data After Delete: ")
print(vars(booking1)) #all attributes will be printed except travelclass

#(b)To Delete complete Object booking1

del booking1

"""Any change made in booking1 will reflect in booking3.
As booking1 has deleted travelClass.So, When we will print vars of Booking3,
travelclass will not be printed """

print("Booking3 Data:")
print(vars(booking3))
print("FROM: ",booking3.fromLocation,"TO: ",booking3.toLocation)






