import sys 

def swap(value1, value2):
    # temp = value1
    # value1 = value2
    # value2 = temp
    # return value1, value2
    return value2, value1

def bubbleSort(arrays):
    length = len(arrays)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if arrays[j] > arrays[j + 1]:
                arrays[j], arrays[j + 1] = swap(arrays[j], arrays[j + 1])

def main():
    scores = [60, 50, 95, 80, 70]

    bubbleSort(scores)

    print(", ".join(map(str, scores)))
    #for score in scores:
    #    print(score, ",", end="")

if __name__ == "__main__":
    main()