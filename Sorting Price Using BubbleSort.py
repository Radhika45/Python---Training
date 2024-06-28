#Dish : name, price, rating
class Dish:
    def __init__(self, name="", price=0, rating=4.5):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("---------DISH------------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("---------------------------")

"""
#List of Dish objects
dish1 = Dish(name="Dal Makhani",price="Rs.450",rating=4.5 )
dish2 = Dish(name="Paneer Makhani ",price="350",rating=5 ) 
dish3 = Dish(name="Noodles ",price="200",rating=4 )
dish4 = Dish(name="Spring Roll ",price="500",rating=5 )
dish5 = Dish(name="Pizza ",price="380",rating=3 )
"""
#Outside the Class

def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):

            if data[j].price > data[j+1].price:
           #if data[j].rating < data[j+1].rating:
           #Swap Operation
                data[j],data[j+1] = data[j+1],data[j]
           
        print()

dishes = [Dish(name="Dal Makhani",price="450",rating=4.5),
          Dish(name="Paneer Makhani ",price="350",rating=5 ),
          Dish(name="Noodles ",price="200",rating=4 ),
          Dish(name="Spring Roll ",price="500",rating=5 ),
          Dish(name="Pizza ",price="380",rating=3 ),
          ]

#for idx in range(len(dishes))
#      dishes[idx].show()
print("DISHES: ")        #A List will be printed
for dish in dishes:
    dish.show()

bubble_sort(dishes)      #Sorting Function

print("Sorted Dishes: ")  #A List after Sorting
for dish in dishes:
    dish.show()
