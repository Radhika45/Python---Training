# (4) Dictionary -> {"a": "", "b": " " }
friends = {"a": "Ram","b":"Shiv","c":"Krishan"}
print(friends, type(friends), id(friends))

#Accesing using Indexing
print(friends["b"])

#Instagram

instagram = {
    "Ram": {"Shiv","Krishan","Vishwas"},
    "Shiv": {"Jay","Sam","kumar"},
    "Sam": {"krishan","Adi","Kapoor"}
}

print(instagram["Shiv"])
print(instagram["Sam"])

print(instagram["Shiv"] & instagram["Sam"])