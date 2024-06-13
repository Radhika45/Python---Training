#CONDITIONAL STATEMENTS i.e If and Else (2)

#Promo Code: ZOMATO is Valid if Condition1 is satisfied
#Condtion1: More than 249
#Condtion2: 50% OFF upto 150

amount = float(input("Enter Amount: "))
promo_code = input("Enter Promo-code: ")

#Nested if-else
if promo_code == "ZOMATO":
    print("Promo-Code is Valid")

    if amount > 249:
        print("Promo Code ZOMATO is applied")
        discount = 0.50 * amount

        if discount >= 150: #If discount value is 150 or greater than it will provide a discoutn of 150 only
            discount = 150
            
        amount -= discount
        print("Discount is: ",discount)
        print("Please Pay: \u20B9",amount)

    else:
        print("Amount is Low , add items worth \u20B9",(249 - amount),"more...")

else:
    print("Promo-code is Invalid")

 
 
