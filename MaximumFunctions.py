#Finding Maximum value using FUNCTIONS
product_prices = [1200, 500, 200, 900, 1000]
salaries = [132,13,4,21]
team =[5755,255,14,99]

def find_max(data):
    max = data[0]
    for idx in range(1,len(data)):
        if data[idx] > max:
            max = data[idx]

    print("Max is: ",max)

find_max(product_prices)
find_max(salaries)
find_max(team)