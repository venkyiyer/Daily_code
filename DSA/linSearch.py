def linearSearch(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1 

print(linearSearch([1,2,3,4,5], 500))