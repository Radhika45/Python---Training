from LinkingRestaurant1 import Dish
from LinkingRestaurant2 import Customer
from LinkingRestaurant3 import Order

dish_menu = [
    Dish(name="Dal Makhani", price= 250 , rating = 4.5),
    Dish(name= "Shahi Panner", price = 400, rating = 4.2),
    Dish(name= "Noodles ", price = 300, rating = 3.5),
    Dish(name= "Pizza ", price = 500, rating = 4.0 ),
    Dish(name= "Dosa ", price = 100, rating = 3.0 )    
]

#Creating Object for Customer class
customer1 = Customer(name="John", phone= 9999911111, email="john@example.com", address="Redwood Shores")
customer2 = Customer(name="Fionna", phone= 9999922222, email="fionna@example.com", address="Country Homes")

"""
#Hard Coding: We as developer are linking objects
order1 = Order(oid=1, dishes=[dish_menu[0], dish_menu[2]], customer=customer1, total=550)
order2 = Order(oid=2, dishes=[dish_menu[2], dish_menu[3], dish_menu[4]], customer=customer1, total=1000)
order1.show()
order2.show()
"""
order1 = Order(oid=1)
order1.link_customer(customer=customer1)
order1.link_dishes(dishes=[dish_menu[0], dish_menu[2]])

order2 = Order(oid=2)
order2.link_customer(customer=customer2)
order2.link_dishes(dishes=[dish_menu[2], dish_menu[3], dish_menu[4]])

order1.show()
order2.show()
