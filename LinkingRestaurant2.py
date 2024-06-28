"""
1 Customer can place many Orders
"""
class Customer:
    def __init__(self, name="N/A", phone="N/A", email="N/A", address="N/A"):
        self.name=name
        self.phone = phone
        self.email = email
        self.address = address

    def show(self):
        print("\n------------CUSTOMER--------------")
        print("Name: {} | Phone: {}".format(self.name, self.phone))
        print("Email: {} | Address: {}".format(self.email, self.address))
        print("----------------------------------")