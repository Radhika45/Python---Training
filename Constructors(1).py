#CONSTRUCTORS

"""Default Constructors"""

class FlightBooking:
    #Default Constuctor
    def __init__(self): 
        print("Self: ",self)
        self.fromLocation="New Delhi"
        self.toLocation = "Bengaluru"
        self.travelDate = "18th June,2024"
        self.numberofTravellers = 1
        self.travelClass = "Economy"
        
#Booking1 is an object in Class Flightbooking
Booking1 = FlightBooking()
print("Booking 1: ",Booking1)
print("Booking 1 Data")
print(vars(Booking1))

Booking2 = FlightBooking()
print("Booking 2: ",Booking2)
print("Booking 2 Data")
print(vars(Booking2))
