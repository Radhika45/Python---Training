#Properties

print("-----Indexing Strings-------")
#quote is a reference variable , when we change the value of quote its hashcode also changes
quote = "Search the candle rather than cursing the darkness"
print("Search the candle rather than cursing the darkness")
print("Id of Quote: ",id(quote))
print("Word at idx[1] :",quote[1])
print("Word at idx[-1] :",quote[-1])
print("Word at idx[-8] :",quote[-8:])

print("-------Appending Strings-------")
quote = quote + "\n" + "Be Exceptional"
print(quote)
print("Id of Quote: ",id(quote))

print("------Multiplicity-----")
data = quote * 3
print(data)

print("-------Concatenation----")
print("the "in quote)


email = input("Enter Your Email: ")
if "@" in email and "." in email:
    print("Email is well formed",email)

else:
    print("Email is not well formed",email)

print("----Searching-------")
print("John","Jenny","Kia","Joe","Jackson","anna","sia")
contacts = ["John","Jenny","Kia","Joe","Jackson","anna","sia"]
search  = input("Enter Search keyword: ")
for contact in contacts:
    if search in contact:
        print(contact)
    #else:
       # print("Contact not found")
