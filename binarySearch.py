
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

listExample = [1, 3, 5, 7, 9, 11, 13]
print(f"O elemento se localiza na posicao: {binarySearch(listExample, 3)}\n")

print(f"O elemento se localiza na posicao: {binarySearch(listExample, -1)}")


