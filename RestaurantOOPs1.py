"""
 Code 3 Objects
 1.Dish : name, price, rating
 2.Menu : name, number_of_dishes, dishes -> (1 Menu can have Many Dishes)
 3.Resturant : name, phone, email, address, operating_hours, ratings, menu -> 1 Resturant can have 1 Menu
"""

#Class for the object Dish
class Dish():
     #Parametrized Constructor, with Default values of argumnets passed to it
     def __init__(self, name="N/A ", price=0, rating=4.5):
          self.name = name
          self.price = price
          self.rating = rating

     def show(self):
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("Dish Data: {}, {}, {}".format(self.name,self.price,self.rating))
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

"""Printing Hashcode of each Object
dish1 = Dish()
print("dish1: ",hex(id(dish1)))
dish2 = Dish("Dal Makhani", 500, 4.5)
print("dish2: ",hex(id(dish2)))
dish3 = Dish("Paneer butter Masala", 300, 5)
print("dish3: ",hex(id(dish3)))"""

"""
#Method to show the Parametrized Function
#(1)
dish1.show()
dish2.show()
dish3.show()
"""

"""
#List of Dishes -> created using Same Class name but Different name for List
Dishes = [ Dish(),
           Dish("Dal Makhani",500,5),
           Dish("Paneer butter Masala",300,5) ]

#Either use idx = 0 or (0,len(Dishes))
for idx in range(0,len(Dishes)):
     Dishes[idx].show()
     """

