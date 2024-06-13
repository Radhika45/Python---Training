#LINEAR SEARCH

instagram_user_name = ["john.j","ram_h","sita.30","ben_a"]
names = ["john johnny","ram bansal","sita kumar","ben"]

user_name = input("Enter user_name to search: ")

#Approach to find user_name using FOR Loop -> 
#(idx) will start from 0 and (len) will start from 1 always
idx = 0

flag = False

for idx in range(0, len(instagram_user_name)): #index will start from 0 till len-1
     # print("Check",user_name,"with",instagram_user_name[idx])
    if user_name==instagram_user_name[idx]:
        print("Name is : ",names[idx])
        break

""" else:
        print("user_name not found")
        break
    """

if flag == False:
    print(user_name,"not found :)")
    

    
