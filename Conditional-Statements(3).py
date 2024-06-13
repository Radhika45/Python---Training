#CONDITIONAL STATEMENTS i.e If and Else (3)

"""
Promo-code 1->ZOMOTO : 20% OFF
                     : min value: 300

Promo-code 2->BINGO : 50 % off
                    :min Value : 500
                    :max discount : 100
"""

promo_code = input ("Enter the Promo Code: ")
amount = float(input("Enter Amount: "))

if promo_code == "ZOMATO":
    print("Zomato can be applied")

#Indentation:Python Enhancement Proposal -> https://peps.python.org/pep-0001/
    if amount > 300:
        discount = 0.20 * amount
        print("ZOMATO applied Successfully.You get a discount of : ",discount)
        print("You can pay: ",amount-discount)

    else:
        print ("Amount is less.Please add items worth",(300-amount),"more...") #i.e min-amount - amount of bill
   

elif promo_code == "BINGO":
    print("Bingo can be applied")

    if amount > 500:
        discount = 0.50 * amount

        if discount >= 100:
            discount = 100
        
        print("BINGO applied Successfully.You get a discount of : ",discount)
        amount -= discount 
        amount = amount + 0.18*amount #Can be GST
        amount += 16.5                #Can be Delievery charges
        #Unicode for Rupee -> https://symbl.cc/en/unicode-table/#devanagari
        print("You can pay: \u20b9",amount-discount)

    else:
        print ("Amount is less.Please add items worth",(500-amount),"more...")
   
else:
    print("Invalid Promo-code")
  