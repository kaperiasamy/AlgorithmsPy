import random

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,  other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second

print(result.x, result.y, sep = ", s")


"""
__add__ for +, translated into a.__add__(y) (y.__radd__(x) is called if x and y are different types)
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for // 
__mod__ for %
__pow__ for ** 
__and__ for &
__or__ for |
__xor__ for ^

__lt__ for <
__gt__ for gt
__le__ for <=
__ge__ for >=
__eq__ for ==
__ne__ for !=

__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to the indexed values
__delitem__ for deleting indexed values 
__iter__ for iteration over objects
__contains__ for in 

__call__ for calling objects as functions 

__repr__ for string representation of the instance
"""

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
    
    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
    
spam = SpecialString("spam")
hello = SpecialString("Hello world!")
eggs = SpecialString("eggs")

print(spam / hello)
spam > eggs 

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    
    def __len__(self):
        return random.randint(0, len(self.cont) * 2)
    
vagueList = VagueList(["A", "B", "C", "D", "E"])
print(len(vagueList))
print(len(vagueList))
print(vagueList[2])
print(vagueList[2])

class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self,  other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self,  other):
        if self.area() > other.area():
            return True
        else:
            return False
        
w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())
print(s1 > s2)
