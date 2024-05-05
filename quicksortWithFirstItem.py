def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] 
        lowerThanPivot = [i for i in array[1:] if i <= pivot]
        higherThanPivot = [j for j in array[1:] if j > pivot]
        return quicksort(lowerThanPivot) + [pivot] + quicksort(higherThanPivot)
    
array = [1, 2, 4, 5, 6, 9, 10, 3, 8]
print(quicksort(array))
    