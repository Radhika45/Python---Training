#.strip() -> It will remove extra space

password = "    hello"
print(password,len(password))

password = "    hello"
p1 = password.strip()
print(p1,len(p1))

data = "0000000344"
print(data)
print(data.strip("0"))

amount = 35.4350000
new_amount = float(str(amount).strip("0"))
print(new_amount , type(new_amount))


#To make any change in the quote line , we must make an new variable
quote = "Search the Candle rather than cursing the darkness"
q1 = quote.replace("the","hello")
print(quote)
print(q1)

message = "No Internet Connection"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

amount = 545
data = str(amount).zfill(8)
print("Data is: ",data)

quote = "Search the Candle rather than cursing the darkness"
idx1 = quote.find("the")
idx2 = quote.find("dark")
print("idx1: ",idx1)
print("idx2: ",idx2)

print(quote[idx1:idx1+4])
print(quote[idx2:])

idx3 = quote.rfind("the")
print(idx3)

print(quote.index("the"))  #FInd the index from Left
print(quote.rindex("the")) #Find the Index from Right




