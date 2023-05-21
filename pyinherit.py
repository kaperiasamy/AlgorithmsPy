
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")
        
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Wolf):
    def bark(self):
        print("Woff!")

fido = Dog("Fido", "Brown")
print(fido.color)
fido.bark()

husky = Dog("max", "Grey")
husky.bark()

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)

B().method()

class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def area(self):
        print(self.width * self.height)

class Rectangle(Shape):
    def perimeter(self):
        print(2 * (self.width + self.height))

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()
