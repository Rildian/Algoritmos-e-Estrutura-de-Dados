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

def binarySearch(list, item):
    
    tooLow = 0
    tooHigh = len(list) - 1 
    
    while tooLow <= tooHigh:
        mid = (tooLow + tooHigh) // 2 
        guess = list[mid]
        if guess == item:
            return mid 
        if guess > item:
            tooHigh = mid - 1
        else:
            tooLow = mid + 1
    return None

listExample = [3, 9 , 10, 89, 2, 1, 30, 120]
newList = quicksort(listExample)
print(f"O elemento se localiza na posicao: {binarySearch(newList, 3)}\n")

print(f"O elemento se localiza na posicao: {binarySearch(newList, -1)}")


