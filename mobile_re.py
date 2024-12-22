import re

mobile = input("Enter a mobile number: ")

x = re.search(r"^\+?[0-9]{1,3}?[-.\s]?[6-9][0-9]{9}$",mobile)

if x:
    print("Valid Mobile Number",x)
else:
    print("Invalid Mobile Number")
