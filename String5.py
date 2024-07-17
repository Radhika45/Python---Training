quote = "Be Exceptional"
print(quote[len(quote)-1])

print("----split()-------")
message = "Hello,How are you. I hope you are doing good"
words = message.split(" ")
print(words)


names = "john, jeim, sia"
words = names.split(", ")
print(words)
print(type(words))

file = open("quote1.txt","r")
#length = len(file.read().spilt())
lines = file.readlines()

print(lines)

total_words = 0
for line in lines:
    total_words += len(line.split(" "))

print("Total_words",total_words)
