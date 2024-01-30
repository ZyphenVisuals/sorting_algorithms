# Introduction

Selection sort is a simple quadratic sorting algorithm that works by always moving the smallest elements towards the beginning of the array.

# Code

We will begin by looking at some Python code:

```python
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
```

The outer loop will iterate through all of the elements of the array, except for the last one, since there's nothing after it.
We will then find the smallest element in the remaining portion of the array, and swap the two elements.

# Visuals

Let's see this in action:

In the first pass, 1 is the smallest element in the array, we will place it at the start.
In the second pass, 2 is the smallest element left, so we place it in the 2nd position.
In the 3rd pass, 3 is the smallest element, which is already at the 3rd position of the array, so we change nothing.
We can now enjoy the rest of the animation.

# Stability

It is important to note that selection sort is _not_ a stable sorting algorithm.

In this example, we can see that after swapping 3 and 2, the threes are now out of order.
