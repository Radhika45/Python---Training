#CONSTRUCTORS

"""Parameterized Constructors"""

class FlightBooking:

    def __init__(self, fromLocation, toLocation, travelDate, numberofTravellers, travelClass):
        print("Self: ",self)
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.travelDate = travelDate
        self.numberofTravellers = numberofTravellers
        self.travelClass = travelClass

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("Booking 1 Data: ")
        print("FROM: ",self.fromLocation,"TO: ",self.toLocation)
        print("~~~~~~~~~~~~~~~~~~~~~~")

#Booking1 is Obj for FlightBooking class
Booking1 = FlightBooking("NewDelhi","Bengaluru","18th June,2024", 1,"Economy")
print("Booking1: ",Booking1)
print("Booking1 Data: ")
print(vars(Booking1))

Booking1.show() #It will print whatever will be present in show()function

#Booking2 is Obj for FlightBooking class
Booking2 = FlightBooking("Chennai", "Bengaluru", "18th June, 2024", 1, "premium")
print("Booking 2:", Booking2)
print("Booking2 data:")
print(vars(Booking2))

Booking2.show() #It will print whatever will be present in show()function

#Booking3 will give error, because it is deafult constructor but we have initialized parametrized cons.
#Booking3 = FlightBooking()      