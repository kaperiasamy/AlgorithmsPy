import sys 

def max(arrays):
    length = len(arrays)
    for i in range(0, length - 1):
        if(arrays[i] > arrays[i + 1]):
            temp = arrays[i]
            arrays[i] = arrays[i + 1]
            arrays[i + 1] = temp
    maxvalue = arrays[length - 1]
    return maxvalue

def main():
    scores = [60, 50, 95, 5, 70]
    maxValue = max(scores)
    print("Max value: ", maxValue)

if __name__ == "__main__":
    main()
