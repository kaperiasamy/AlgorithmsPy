import sys

def printInCSV(arrays):
    print(", ".join(map(str, arrays)))

def main():
    scores = [90, 70, 50, 80, 60, 85]
    length = len(scores)

    #Create a new temp array, length = length + 1
    tempArray = [0 for _ in range(length + 1)]

    for i in range(0, length):
        tempArray[i] = scores[i]

    tempArray[length] = 75
    scores = tempArray

    length = len(scores)

    printInCSV(scores)

if __name__ == '__main__':
    main()