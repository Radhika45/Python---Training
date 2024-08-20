#Method 1 to Open
file = open("ipl-data-2022.csv","r")

#List of Strings
lines = file.readlines()

for line in lines:
    print(line)


#Method 2 To open
"""
with open("ipl-data-2022.csv","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)"""

