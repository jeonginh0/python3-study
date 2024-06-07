# Oop4.py

class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return "Meow!"

class Dog(Animal):
    def talk(self):
        return "Woof! Woof!"

animals = [Cat('미키'), Dog('동동이')]
for animal in animals:
    print(animal.name + ": " + animal.talk())

a= [1,2,3]
b= [4,5,]
c= [7,8,9]
print([[sum(k), len(k)]for k in zip(a,b,c)])