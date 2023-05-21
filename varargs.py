def fn(namedArg, *args):
    print(namedArg)
    print(args)

fn(1, 2, 3, 4, 5)

def func(x, y = 7, *args, **kwargs):
    # kwargs: dictionary
    # args: tuple
    print(kwargs)
    print(args)
    print(x, y)

func(2, 3, 4, 5, 6, a = 7, b = 8)

def minimum(*args):
    min = args[0]
    for n in args:
        # print(n)
        if n < min:
            min = n
    return min

print(minimum(8, 13, 4, 42, 120, 7))

nms = {1, 2, 3, 4, 5, 6}
nms = {0, 1, 2, 3} & nms
nms = filter(lambda x: x > 1, nms)
print(len(list(nms)))

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
    
print(power(2, 3))

a = (lambda x: x * (x + 1))(6)
print(a)

ns = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x % 2 == 0, ns))
print(res)

def kwargfn(**kwargs):
    print(kwargs["zero"])

kwargfn(a = 0, zero = 8)
