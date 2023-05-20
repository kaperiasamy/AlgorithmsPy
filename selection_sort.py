import sys

def swap(value1, value2):
    return value2, value1

def printInCSV(arrays):
    print(", ".join(map(str, arrays)))

def sort(arrays):
    length = len(arrays) - 1
    # Index of the selected minimumMINIMUM_FOMINIMUM_FONT_SIZE
    minIndex = 0 

    for i in range(0, length):
        minIndex = i
        # Minimum value of each loop as the first element 
        minValue = arrays[minIndex] 
        for j in range(i, length):
            # Compare with each element 
            # if it is less than the minimum value, 
            # exchange the minIndex
            if minValue > arrays[j + 1]:
                minValue = arrays[j + 1]
                minIndex = j + 1

        # If the minimum index changes, 
        # the current minimum is 
        # exchanged with the minIndex
        if i != minIndex:
            arrays[i], arrays[minIndex] = swap(arrays[i], arrays[minIndex])

def main():
    scores = [60, 80, 95, 50, 70]
    sort(scores)
    printInCSV(scores)

if __name__ == "__main__":
    main()

"""
https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14

https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

"""