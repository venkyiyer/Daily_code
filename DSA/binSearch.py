def binarySearch(arr, value):
    get_mid_element = len(arr)/2
    if arr[get_mid_element] > value:
        arr1 = arr[get_mid_element:]
        for i in range(len(arr1)):
            if i == value:
                return i
    elif:
        arr1 = arr[:get_mid_element]
        for i in range(len(arr1)):
            if i == value:
                return i
    
    else:
        