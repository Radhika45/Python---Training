#String is Immutable Hashcode of everything will reamin same

quote = "Be Exceptional"
print("=====Be Exceptional======")
print("Hashcode of Quote is: ",id(quote))
s1 = quote.upper()
print("----------upper()----------")
print("1.Quote is: ",quote)
print("1.Hashcode of quote is: ",id(quote))

print("----------lower()----------")
s2 = quote.lower()
print("2.Quote is: ",quote)
print("2.Hashcode of quote is: ",id(quote))

print("s1 : ",s1)
print("s2 : ",s2)

print("----------capitalize()----------")
s3 = quote.capitalize()
print("s3: ",s3)

print("----------title()----------")
s4 = quote.title()
print("s4: ",s4)

print("----------swapcase()----------")
quote = "Be Exceptional"
s5 = quote.swapcase()
print("s5 : ",s5)