#OLA UBER PROBLEM

#Customer - name, phone, email, address, gender, age

from Ola2 import Driver


class Customer:
    def __init__(self,name="N/A", phone="N/A", email="N/A", address="N/A", gender="N/A", age="N/A"):
        self.name= name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    def add_customer_details(self):
        print(">>--------------CUSTOMER DETAILS------------------")
        self.name = str(input("Enter Customer Name: "))
        self.phone= int(input("Enter Customer Phone: "))
        self.email= input("Enter Customer Email: ")
        self.address = input("Enter Customer Address: ")
        self.gender = str(input("Enter Customer Gender: "))
        self.age = int(input("Enter Customer Age: "))

    def show(self):
        print("-----------------CUSTOMER----------------------")
        print("Customer Name: {} | Customer Phone: {}".format(self.name,self.phone))
        print("Customer Email: {} | Customer Address: {}".format(self.email,self.address))
        print("Customer Gender {} | Customer Age {}".format(self.gender,self.age))
        print("---------------------------------------")

    def to_csv(self):
        data = "{},{},{},{},{},{}\n".format(self.name,self.phone,self.email,self.address,self.gender,self.age)
        return data
    
    
"""
driver = Driver()
driver.add_driver_details()

customer = Customer()
customer.add_customer_details()

driver.show()
customer.show()

"""