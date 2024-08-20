def upgrade_to_meal(func):

    def inner(amount, taxes,meal_plan):
        
        if meal_plan == 1:
            print("Upgrading to Medium Meal...")
            print("+ Added Coke")
            print("+ Added Fries")
            amount += 100
            taxes = 0.18

        elif meal_plan == 2:
            print("Upgrading to Large Meal...")
            print("+ Added Large Coke")
            print("+ Added Large Fries")
            print("+ Added Large Fries")
            amount += 200
            taxes = 0.20

        return func(amount, taxes,meal_plan)
    
    return inner

@upgrade_to_meal
def buy_burger (amount, taxes, meal_plan =0):
    return amount + (amount * taxes)

amount_to_pay = buy_burger(100, 0.5, 1)
print("Amount to pay: ", amount_to_pay)
