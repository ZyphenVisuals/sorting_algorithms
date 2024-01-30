# Introduction

Bubble sort is a simple quadratic sorting algorithm that works by swapping neighboring elements when they're out of order.
In practice, bubble sort is a very slow sorting algorithm, being used almost exclusively in education.

# Code

We will begin by looking at some Python code:

```python
def bubbleSort(array):
  # count how many elements are sorted
  for i in range(len(array)):
    # loop to compare unsorted elements
    for j in range(0, len(array) - i - 1):
      # swap adjacent elements if in wrong order
      if array[j] > array[j + 1]:
        array[j], array[j+1] = array[j+1], array[j]
```

The outer loop represents the amount of passes we must do to ensure the array is ordered. After each pass, one more element at the end of the array is guaranteed to be in the correct spot.
The inner loop goes through all of the unsorted elements of the array and swaps neighboring elements when they're out of order.

# Visuals

Let's see this in action:

Notice how in this case, the array is already sorted after the second pass. A possible optimization is stopping the algorithm if during any given pass we haven't executed any swaps.

# Stability

An important property of bubble sort is that it is a stable sorting algorithm, meaning that elements of the same value will remain in their original order.

By only swapping neighboring elements, it's impossible for an element to "overtake" another element of equal value.
