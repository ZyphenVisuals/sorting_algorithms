def selectionSort(array):
    for i in range(len(array)-1):
        # find the smallest value in the remaining array
        min_id = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_id]:
                min_id = j
        # if we found a smaller value, swap
        if min_id != i:
            array[i], array[min_id] = array[min_id], array[i]