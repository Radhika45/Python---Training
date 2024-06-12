# Restaurant Model View Controller

#Add to Cart is made using LIST -> which can be either homogeneous or hetrogeneous
cart = []
quantity = []
price = []

#Menu is made using DICTIONARY
menu = {
    #Name of Dish -> KEY
    #Price of Dish -> VALUE
    "Burger": 100, 
    "Pizza": 200,
    "Momos": 300,
    "Noodles": 400

}

#Introduction to Model Page
print("~~~~~~~~~~~~~~~~~~~\n")
print("Welcome To Foodies")
print("~~~~~~~~~~~~~~~~~~~\n")
print(" Food Menu ")

#Calling "menu" variable
print(menu) 
print("~\n")

#Loop for adding items-> add adequate space in while loop
while True:
    item = input("Enter Food Item to add in Cart or 0 to quit: ")

    if item == "0":
       break

    qty = int(input("Enter Quantity for item: "))
    quantity.append(qty)

    cart.append(item) #Until while is true , whatever is added to ITEM will be added to cart through Append
    price.append(menu[item]*qty)

print("Cart Contains: ")
print(cart)
print("Quantity: ")
print(quantity)
print("Prices are:")
print(price)

print("Items in Cart: ", len(cart)) #Size of Cart
print("Amount to Pay: ", sum(price)) #Sum of Cart