#Decorators :) -> Design Pattern
"""
1.Create a Function , which takes function as input
2.Create A Inner Function , ehich should have same signature of the target function
3. execute the passed function from the inner function
4.return the inner function from outer function
5. to decorate any function use @function
"""

def compute_taxes(func):

    def inner(amount, taxes):
        if amount > 0 and amount <= 10000:
            taxes = 0.18  #Update Taxes
        elif amount > 10000:
            taxes = 0.25  #Update Taxes
        else: 
            print("Invalid Amount")

        return func(amount, taxes)
    
    return inner

@compute_taxes
def pay (amount,taxes):
    return amount + (amount*taxes)

amount_to_pay = pay(2000, 0)
print("Amount to pay: ",amount_to_pay)
