#FILE HANDLING 

quote1 = "Search the candle raather than cursing the darkness\n"
quote2 = "Be exceptional\n"

#file = open("quote.txt","w")  w -> write operation, a ->append operation , It will create txt file named quote.txt
file = open("quote1.txt","a")
file.write(quote1)
file.write(quote2)

#Free Memory Resource once,you have used file
file.close()

print("Data Written....")


