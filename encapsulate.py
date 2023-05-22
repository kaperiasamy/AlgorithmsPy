class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
    
queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

class Spam:
    __egg = 7

    def printEgg(self):
        print(self.__egg)

s = Spam()
s.printEgg()
print(s._Spam__egg)
# print(s.__egg) # throws error: AttributeError: 'Spam' object has no attribute '__egg'

class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1
        if self._lives == 0:
            print("Game Over")

p = Player("Cyberpunk77", 3)
p.hit()
p.hit()
p.hit()
