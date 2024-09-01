#Write a Python script that prints prime numbers less than 20

print("Prime numbers between 1 and 20 are:")
given_numbers =20
for num in range(given_numbers):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)