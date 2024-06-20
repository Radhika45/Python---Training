from Ola2 import Driver
from Ola3 import Customer
from Ola4 import Ride

#DRiver Application
driver = Driver()
driver.add_driver_details()

#Customer Application
customer = Customer()
customer.add_customer_details()

#Server
ride = Ride()
ride.add_ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("RIDE BOOKED....")
ride.show()
