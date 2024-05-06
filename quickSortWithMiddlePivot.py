def quicksort(array, indexOfThelowest, indexOfThehighest):
    if (indexOfThelowest >= indexOfThehighest):
        return 
    
    pivot = array[(indexOfThelowest + indexOfThehighest)//2]       
    i = indexOfThelowest - 1
    j = indexOfThehighest + 1
    while(True):
        while(True):               
            i += 1
            if(array[i] >= pivot):
                break
        while(True):               
            j -= 1
            if(array[j] <= pivot):
                break
        if(i >= j):
            break
        
        array[i], array[j] = array[j], array[i]
    
    quicksort(array, indexOfThelowest, j)
    quicksort(array, j + 1, indexOfThehighest)

    return array

    
array = [1, 2, 4, 5, 6, 9, 10, 3, 8] 
print(quicksort(array, 0, (len(array) - 1)))