def selectionsort(customList):
    for i in range (len(customList)):
         min_value = i
         for j in range(i+1, len(customList)):
            if customList[min_value] > customList[j]:
                 min_value = j
            customList[i], customList[min_value] = customList[min_value], customList[i]
    print(customList)


def insertionsort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
       


insertionsort([5,7,9,1,4,2,6,3])
