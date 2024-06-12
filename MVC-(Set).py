# (3) Set -> { } It does not repeat same values , output results in unorderd form

friends_1 = {"Ram", "Krishan", "Shiv", "Ram","Shiv"}
print(friends_1, type (friends_1), id(friends_1))

friends_2 = {"Sita","Gita","Ram","Mita"}

mutual_friends = friends_1 & friends_2

print(mutual_friends)

#Set -> It does support Indexing , else it works on Hashing
#print(friends_1[0])


