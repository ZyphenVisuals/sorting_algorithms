def bubbleSort(array):
  # count how many elements are sorted
  for i in range(len(array)):
    # loop to compare unsorted elements
    for j in range(0, len(array) - i - 1):
      # swap adjacent elements if in wrong order
      if array[j] > array[j + 1]:
        array[j], array[j+1] = array[j+1], array[j]