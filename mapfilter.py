def addFive(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(addFive, nums))
print(result)

result = list(map(lambda x: x + 5, nums))
print(result)

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
