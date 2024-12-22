class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute 
        self.__age = age    

    def get_name(self):  
        return self.__name

    def set_name(self, name): 
        if len(name) > 0:
            self.__name = name
        else:
            print("Name cannot be empty!")

    def get_age(self):  
        return self.__age

    def set_age(self, age):  
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")


person = Person("Ram Kumar", 30)


print(person.get_name())  
print(person.get_age())   


person.set_name("Preeti")
print(person.get_name()) 
person.set_age(50)
print(person.get_age())   

# Attempt invalid values
person.set_name("")  
person.set_age(-5)   
