import re

email = input("Enter any Email: ")

x = re.search(".*a.*.com",email)

print(x)

if(x):
    print("Email Pattern Found",x)

else:
    print("Pattern not Found")