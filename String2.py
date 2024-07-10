#Properties

#quote is a reference variable , when we change the value of quote its hashcode also changes
quote = "Search the candle rather than cursing the darkness"
print(id(quote))
print(quote[1])
print(quote[-1])
print(quote[-8:])

quote = quote + "\n" + "Be Exceptional\n"
print(quote)
print(id(quote))

data = quote * 3
print(data)

print("the "in quote)

email = input("Enter Your Email: ")
if "@" in email and "." in email:
    print("Email is well formed",email)

else:
    print("Email is not well formed",email)

contacts = ["John","Jenny","Kia","Joe","Jackson","anna","sia"]
search  = input("Enter Search keyword: ")
for contact in contacts:
    if search in contact:
        print(contact)
    #else:
       # print("Contact not found")
