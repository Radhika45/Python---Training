#OLA UBER PROBLEM

#Driver - name,phone,email,vehicle[1 driver 1 vehicle],gender,age,rating,license_number

from Ola1 import Vehicle
class Driver:

    def __init__(self,name="N/A",phone="N/A",email="N/A"
                 ,gender="N/A",age="N/A",rating="N/A",license_number="N/A",
                 vehicle="N/A"):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender= gender
        self.age = age
        self.rating = rating
        self.license_number = license_number
        self.vehicle = vehicle

    def add_driver_details(self):
        print("-----------DRIVER DETAILS-----------------")
        self.name = str(input("Enter Driver Name: "))
        self.phone = int(input("Enter Driver Phone: "))
        self.email = input("Enter Driver email: ")
        self.gender = str(input("Enter Driver gender: "))
        self.age = int(input("Enter Driver age: "))
        self.rating = int(input("Enter Driver rating: "))
        self.license_number = int(input("Enter Driver license_number: "))
        #1 to 1 Mapping
        print("-----------VEHICLE DETAILS-----------------")
        self.vehicle = Vehicle()
        self.vehicle.add_vehicle_details()


    def show(self):
        print("-----------------DRIVER----------------------")
        print("Driver Name : {} | Driver Number: {}".format(self.name,self.phone))
        print("Driver email: {} | Driver gender: {}".format(self.email,self.gender))
        print("Driver age: {} | Driver rating: {}".format(self.age,self.rating))
        self.vehicle.show()
        print("---------------------------------------")  
"""
driver = Driver()
driver.add_driver_details()
driver.show()
"""