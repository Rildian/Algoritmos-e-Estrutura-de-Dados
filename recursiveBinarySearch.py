def recursiveBinarySearch(arr, low, high, item):
    mid = (high + low)//2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return recursiveBinarySearch(arr, low, mid-1, item)
    elif arr[mid] < item:
        return recursiveBinarySearch(arr, mid + 1, high, item)
    else:
        return - 1 # if element not found


array = [2, 3, 4, 10, 40] # only works if sorted
print(recursiveBinarySearch(array, 0, len(array) - 1, 10))
