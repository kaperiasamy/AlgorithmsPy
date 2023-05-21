class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("woof!")

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + "(Level " + self.level + ")") 

felix = Cat('Ginger', 4)
rover = Cat('Dog-colored', 4)
stumpy = Cat('Brown', 3)

print(felix.color)

fido = Dog("Fido", "Brown")
print(fido.name)
fido.bark()

name = input()
level = input()
player = Player(name, level)
player.intro()
