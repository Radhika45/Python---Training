#Write a Python program to convert temperatures to and from Celsius, Fahrenheit.[ For1mula: c/5 = f-32/9]

print("1 - > Celsious to Farhentheit")
print("2 - > Farhenheit to Celsious")

user = int(input("Enter either 1 or 2: "))

if user == 1:
    c1 = float(input("Enter Celcious: "))
    f1 = (c1 * 1.8) + 32
    print("%0.1f Celcious is equal to %0.1f Frahenheit." %(c1, f1))

elif user == 2:
    f2 = float(input("Enter farhenheit: "))
    c2 = (f2 - 32) / 1.8
    print ("%0.1f Frahenheit is equal to %0.1f Celsious." %(f2, c2))

else:
    print("Enter either 1 or 2 only")





