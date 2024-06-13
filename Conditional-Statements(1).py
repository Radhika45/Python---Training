#CONDITIONAL STATEMENTS i.e If and Else (1)

'''Condition1: 
You can apply a Promocode only if the minimum payable amount is Rs.500,
else no discount will be offered.'''

promo_code = "GET200"
min_amount = 500

amount = float(input("Enter Amount: "))

#Condiotional Statement
if amount > min_amount:
    print("You can apply Promocode",promo_code)
    amount -= 200 #amount = amount -200
    print("Promo Code Applied Succesfully.Please pay: \u20A8",amount) #here \u20B9 is unicode of Rupees
else:
    print("You cannot apply Promocode",promo_code)
    print("Add Items worth", (min_amount - amount),"more...")

