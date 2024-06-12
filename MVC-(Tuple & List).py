#MULTI VALUE CONTAINER

# (1) Tuple -> ( ) Immutable i.e cannot be changed
friends = ("Ram", "Krishan", "Shiv")
print(friends, type (friends), id(friends))
 
 #Extracting using Index of friends

print(friends[0], type(friends[0]), id(friends[0]))
print(friends[1], type(friends[1]), id(friends[1]))
print(friends[2], type(friends[2]), id(friends[2]))

 #Making a Change in Tuple
friends[1] = 20
print(friends, type (friends), id(friends))

# (2) List -> [ ] Mutable i.e Changes can be made
friends = ["Ram", "Krishan", "Shiv"]
print(friends, type (friends), id(friends))

 #Making a change 

friends[1] = 20
print(friends, type (friends), id(friends))



