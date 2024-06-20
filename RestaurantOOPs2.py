"""
 Code 3 Objects
 1.Dish : name, price, rating
 2.Menu : name, number_of_dishes, dishes -> (1 Menu can have Many Dishes)
 3.Resturant : name, phone, email, address, operating_hours, ratings, menu -> 1 Resturant can have 1 Menu
"""

from RestaurantOOPs1 import Dish


class Menu:
    def __init__(self, name="N/A ", number_of_dishes=0, menu_dishes=[]):
        self.name= name
        self.number_of_dishes = number_of_dishes
        self.menu_dishes = menu_dishes
        
    def show(self):
        print("MENU: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {} | {}".format(self.name, self.number_of_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("Dishes:")
        for idx in range (0,len(self.menu_dishes)):
            self.menu_dishes[idx].show()

"""
dishes =[
    Dish(),
    Dish("Dal Makhani",250,4.5),
    Dish("Shahi Panneer",300,5)

]


menu = Menu(
    name ="Indian Veg",
    number_of_dishes = len(dishes),
    menu_dishes = dishes
)


menu.show()

"""
        