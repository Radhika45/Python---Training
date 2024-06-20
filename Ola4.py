#OLA UBER PROBLEM

#ride - customer[1 to 1],date, time, from_location, to_location, distance, fare, driver[1to1]

from Ola3 import Customer
from Ola2 import Driver


class Ride:
    def __init__( self,customer="N/A",date="N/A", time="N/A", from_location="N/A", to_location="N/A", distance="N/A", fare="N/A", driver="N/A"):
        self.customer = customer
        self.date = date
        self.time = time
        self.from_location = from_location
        self.to_location = to_location
        self.distance= distance
        self.fare = fare
        self.driver= driver
        
        
    def add_ride_details(self):
        
        print(">>>----------------RIDE DETAILS------------------")
        self.date= input("Enter Date: ")
        self.time= input("Enter Time: ")
        self.from_location = input("Enter From_location : ")
        self.to_location = input("Enter To_location  ")
        self.distance= input("Enter Distance: ")
        self.fare= input("Enter Fare: ")
        print("-------------------------------------")
        

    def link_customer(self,customer):
        self.customer = customer

    def link_driver(self,driver):
        self.driver = driver

    def show(self):
        print("-----------------RIDE ----------------------")
       
        print("Date: {}".format(self.date))
        print("Time: {} | From_location: {}".format(self.time,self.from_location))
        print("To_location: {} | Distance: {}".format(self.to_location,self.distance))
        print("Fare: {} ".format(self.fare))
        self.customer.show()
        self.driver.show()
        print("---------------------------------------")  

    

"""
driver = Driver()
driver.add_driver_details()

customer = Customer()
customer.add_customer_details()
driver.show()
customer.show()
"""



    