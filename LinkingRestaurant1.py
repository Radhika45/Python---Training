"""OOPs Case study - FOOD DELIVERY APP
Customer
Dish
Order

Condition - 1 Customer can place many orders.
            1 Order can have many dishes.
"""

class Dish:
    def __init__(self, name="N/A", price=0, rating=1.5):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("\n---------DISH------------")
        print("Name: {} | Price: {} | Ratings: {}".format(self.name, self.price, self.rating))
        print("---------------------------")