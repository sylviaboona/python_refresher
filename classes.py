from ast import Num


class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point1 = Point()
point1.draw()

#CONSTRUCTORS - a function called at the time of creating an object
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

coordinate1 = Coordinates(5, 10)
print(coordinate1.x)

class Person:
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def talk(self):
        print(f"My name is {self.name}. I speak {self.language}...")

person1 = Person('Sylvia', 'Runyakitara')
person1.talk()

#INHERITANCE
class Animal:
    def walk(self):
        print('walk')

class Dog(Animal):
    def bark(self):
        print('bark')

class Cat(Animal):
    def be_annoying(self):
        print('I am super annoying')


