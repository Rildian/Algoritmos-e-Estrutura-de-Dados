def searchForTheLowest(array):
    lowest = array[0]
    lowestIndex = 0
    for i in range(1, len(array)):
        if array[i] < lowest:
            lowest = array[i]
            lowestIndex = i
    return lowestIndex

def selectionSort(array):
    newArray = []
    for j in range(len(array)):
        indexOfTheLowest = searchForTheLowest(array)
        newArray.append(array.pop(indexOfTheLowest))
    return newArray

array = [3, 4, 5, 12, 1, 4, 6, 7]
print(f"Array ordenado: {selectionSort(array)}")


