def decorate(func):
    def wrap(): # Nested function 
        print("**********")
        func()
        print("**********")
    return wrap

@decorate
def printText():
    print("Hello text!!!")

#decorated = decor(printText)
#decorated()

printText()

def decor(fn):
    def wrap(n): # Nested function 
        print("***")
        fn(n)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #", num)

invoice(input())
