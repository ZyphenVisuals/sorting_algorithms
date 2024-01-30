def insertionSort(array):
    # Start from the second item
    for step in range(1, len(array)):
        aux = array[step]
        # Loop through all previous items
        j = step - 1
        # Move aux left until we find a smaller element
        while j >= 0 and aux < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = aux
# Modified from programiz.com