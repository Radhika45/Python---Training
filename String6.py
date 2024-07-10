messages = [
    {"sender": "99155 71355",
     "receiver": "9876544421",
     "conversaton":[
         "hello",
         "How are you",
         "Its Friday",
         "Lets Party"
     ]
     },
    
    {"sender": "99155 71355",
     "receiver": "9876544421",
     "conversaton":[
         "Beta",
         "How are you,Mummy",
         "Lets go to Market",
         "Lets Party"
     ]
     }
]

search_keyword= input("Enter Word to search: ")
#Hw
for search in messages:
    if search == search_keyword:
        print("Word Found: ",messages[search])