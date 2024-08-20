#GENERATORS IN PYTHON


"""
def fetch():
    file = open("ipl-data-2022.csv","r")
    lines = file.readlines()

    for line in lines:
        #Return is a Termination Statement as when it will return a line , the output will be returned as first line only
        return line
        
result = fetch()
print("Result: ",result)"""

def fetch():
    file = open("ipl-data-2022.csv","r")
    lines = file.readlines()

    for line in lines:
        yield line

#if a function, yields, it means we get Generator in return       
result = fetch()
print("Result: ",result)

print(next(result))
print(next(result))

while True:
    data = next(result, "Nothing")
    print(data)
    if data == "Nothing":
        break

