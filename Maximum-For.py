#Finding Maximum value using FOR loop
product_prices = [1200, 500, 200, 900, 1000]
salaries = [132,13,4,21]
team =[5755,255,14,99]

#max in product_prices
max = product_prices[0] #1200
for idx in range (1,len(product_prices)):
    if product_prices[idx]> max:
        max = product_prices[idx]

print("max is: ",max)

#max in salaries
max = salaries[0] #132
for idx in range (1,len(salaries)):
    if salaries[idx]>max:
        max = salaries[idx]

print("Max is: ",max)

#max in team
max = team[0]    #5755
for idx in range (1,len(team)):
    if team[idx]>max:
        max = team[idx]

