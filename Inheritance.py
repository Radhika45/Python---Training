# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def speak(self):
       print(f"{self.name} barks.")
       
# Derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Polymorphism in action
def animal_sound(animal):
    print(animal.speak())

# Testing Inheritance
d1 = Dog("Buddy")
c1 = Cat("Kitty")

print(d1.speak()) 
print(c1.speak())  

#Polymorphism
animal_sound(d1)  
animal_sound(c1)  


