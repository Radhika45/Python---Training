from RestaurantOOPs1 import Dish
from RestaurantOOPs2 import Menu

class Restaurant:
    def __init__(self,name="N/A",phone="N/A",email="N/A",address="N/A",operating_hours="10-12",ratings=4.5,menu ="n/A"):
        self.name=name 
        self.phone=phone
        self.email=email
        self.address=address 
        self.operating_hours=operating_hours
        self.ratings=ratings
        self.menu=menu 

    def show(self):
        print("RESTAURANT")  
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("Resturant: {} |{} |{} ".format(self.name,self.phone,self.email))
        print("Address: {} |{} |{}".format(self.address,self.operating_hours,self.ratings))
        print("~~~~~~~~~~~~~~~~~~~~~\n")

        self.menu.show()


"""
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]



menu = Menu(
    name="Indian Veggie Delight", 
    number_of_dishes=len(dishes), 
    menu_dishes=dishes)
"""


restaurant = Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        )

restaurant.show()

"""
Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        ).show()
        
"""