# Introduction

Insertion sort is a simple quadratic sorting algorithm that is often described as functioning similarly to the way a human would sort cards in their hand.
This is done by considering a certain portion of the cards ordered, and then _inserting_ the other cards one by one in their correct spot.

# Code

We will begin by looking at some Python code:

```python
def insertionSort(array):
    # Start from the second item
    for step in range(1, len(array)):
        aux = array[step]
        # Loop through all previous items
        j = step - 1
        # Compare aux with each element on the left of it until an element smaller than it is found
        while j >= 0 and aux < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = aux
# Modified from programiz.com
```

The outer loop will iterate through all of the elements of the array starting from the second one. We consider the first element to be always sorted, as we have nothing to compare it to.
We then save this value in an auxiliary variable and start moving to the left until we reach a value smaller than it, effectively pushing all other elements to the right as we go.
Once we found a value smaller than the one in our auxiliary variable, we place the auxiliary value back into the array in it's correct spot.

# Visuals

Let's see this in action:

In this case, since the 2 is smaller than the 3, the 3 will be placed after it, effectively staying unmoved and having no effect on the array.
However, in the case of the 1, it never encounters something smaller than it, so it keeps moving to the left until it reaches the start of the array, where it gets placed. Notice how as it moves to the left, the elements it moves past get pushed to the right.

# Stability

An important property of insertion sort is that it is a stable sorting algorithm, meaning that elements of the same value will remain in their original order.

In this example, we can see that after 4 is compared an equal element, it gets put back in its original position.
