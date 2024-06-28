# 1 Order can have Many Dishes
# But 1 Order can have only 1 Customer

class Order:

    def __init__(self, oid =0, dishes=None, customer=None, total = 0):
        self.oid = oid
        self.dishes = dishes
        self.customer = customer
        self.total = total

    def show(self):
        print("\n-----------ORDER------------------")
        print("ID: {} | Total: {}".format(self.oid,self.total))
        print("--------------------------------")

        print("Order Placed By: ")
        self.customer.show()

        print("--------Order Dishes-----------")
        for dish in self.dishes:
            dish.show()

        print("--------------------------------")

    def link_customer(self, customer):
        self.customer = customer

    def link_dishes(self, dishes):
        self.dishes = dishes
        
        for dish in dishes:
            self.total += dish.price
        

        
    