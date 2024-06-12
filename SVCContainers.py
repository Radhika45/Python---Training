#CONTAINERS

#Single Vlaue Containers

#Create Statement -> We are creating a SVC in RAM

user_name = "radhika" # Strings in double quotes

#Read Statement -> It will read data inside a SVC

print(user_name,id(user_name),type(user_name))

#Update Statement

user_name = 99       # Numbers without Quotes

#Re-printing after Updation
print(user_name,id(user_name),type(user_name))

#Delete Statement
del user_name

#Re-printing after Deletion -> It will give error as no variable for user_name exits now
print(user_name,id(user_name),type(user_name))


