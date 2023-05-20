def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

def isPrime(x):
    if x < 2: return False
    elif x == 2: return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True

def primeGenerator(a, b):
    for n in range(a, b):
        if isPrime(n): 
            yield n

def makeWord():
    word = ""
    for ch in "spam":
        word += ch
        yield word

print(list(makeWord()))

f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

for i in countdown():
    print(i)