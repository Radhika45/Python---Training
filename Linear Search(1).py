#LINEAR SEARCH

instagram_user_name = ["john.j","ram_h","sita.30","ben_a"]
names = ["john johnny","ram bansal","sita kumar","ben"]

user_name = input("Enter user_name to search: ")

#Approach to find User_name using If,Elif and Else statement

idx = 0 #Always initialize idx with 0

if user_name == instagram_user_name[idx]:
    print("Name is : ",names[idx])

elif user_name == instagram_user_name[idx+1]:
    print("Name is : ",names[idx +1])
elif user_name == instagram_user_name[idx+1]:
    print("Name is : ",names[idx +2])
elif user_name == instagram_user_name[idx+1]:
    print("Name is : ",names[idx +3])

else:
    print("Cannot Find user_name")



