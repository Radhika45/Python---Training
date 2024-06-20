#OLA UBER PROBLEM

#Driver - name,phone,email,vehicle[1 driver 1 vehicle],gender,age,rating,license_number
#Vehile - reg_number, brand, model, color
#Customer - name, phone, email, address, gender, age
#ride - Customer[1 to 1], date, time, charges, distance, booking_from, booking_destination,


class Vehicle:
    def __init__(self,reg_number="N/A", brand="N/A", model="N/A", color="white"):
        self.reg_number = reg_number
        self.brand = brand
        self.model = model
        self.color = color

    def add_vehicle_details(self):
        self.reg_number = input("Enter Registration Number: ")
        self.brand = input("Enter Brand Number: ")
        self.model = input("Enter Model of Vehicle: ")
        self.color = str(input("Enter Color of Vehicle: "))

    def show(self):
        print("-----------------VEHILCLE----------------------")
        print("Vehicle Registration Number: {} | Vehicle Model Number: {}".format(self.reg_number,self.model))
        print("Vehicle Brand : {} | Vehicle Color: {}".format(self.brand,self.color))
 
        print("---------------------------------------")
#vehicle = Vehicle(reg_number="PB10AB99",model="TVS")
"""
vehicle= Vehicle()
vehicle.add_vehicle_details()
vehicle.show()
"""