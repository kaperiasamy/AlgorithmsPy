from operator import le
import sys

def printInCSV(arrays):
    print(", ".join(map(str, arrays)))

def sort(arrays):
    length = len(arrays)
    for i in range(0, length - 1):
        # take unsorted new elements
        insertElement = arrays[i]
        # Inserted position
        insertPosition = i

        for j in range(insertPosition - 1, -1, -1):
            # if the new element is smaller than the sorted
            # element, it is shifted to the right
            if insertElement < arrays[j]:
                arrays[j + 1] = arrays[j]
                insertPosition -= 1
        
        # insert the new element
        arrays[insertPosition] = insertElement

def main():
    scores = [80, 70, 60, 50, 95]
    sort(scores)
    printInCSV(scores)

if __name__ == '__main__':
    main()