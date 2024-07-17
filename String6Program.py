messages = [
    {
        "sender" : "9999",
        "receiver" : "1111",
        "conversation" : [
            "Hello",
            "How are you",
            "Let's Party"
        ]
    },
    {
        "sender" : "7777",
        "receiver" : "2222",
        "conversation" : [
            "Hi",
            "Where are you",
            "Let's Meet"
        ]
    },
    {
        "sender" : "9999",
        "receiver" : "2222",
        "conversation" : [
            "This is John",
            "When are you coming ?",
            "Let's go out for dinner"
        ]
    },
]

search_keyword = input("\nEnter word to search: ")
print(" ")

flag = False

for word in messages:
    sender = word["sender"]
    receiver = word["receiver"]
    conversation = word["conversation"]

    for data in conversation:
        if search_keyword in data:
            print("Sender: {} | Receiver: {}".format(sender,receiver))
            print("Message: {}".format(data))
            print("Word found at index: {}".format(data.find(search_keyword)))
            print("~")
            flag = True
        
if flag == False:
    print("Word not Found")