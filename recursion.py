def factorial(x):
    if x == 1:
        return 1 # Base case, exit condition 
    else:
        return x * factorial(x - 1)
    
print(factorial(5))

def isEven(x):
    if x == 0:
        return True
    else:
        return isOdd(x - 1)
    
def isOdd(x):
    return not isEven(x)

print(isOdd(7))
print(isEven(25))

def convert(n):
    if n == 0 or n == 1:
        return n
    else:
        return (n % 2 + 10 * convert(n // 2))

n = int(input())
print(convert(n))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(4))
