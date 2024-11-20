"""
Author: Paul Sommers
Date written: 11/20/2024
Assignment: Exercise 6-6 Define and Test myRange Function
Short Desc: This program defines `myRange`, a function that emulates Python's built-in `range` function, but returns a list. 
            It supports the same parameters as `range` (start, stop, step) and handles default values.
"""

# Define myRange function
def myRange(start=None, stop=None, step=None):
    # Handle case where only stop value is provided
    if stop is None and step is None:
        stop = start
        start = 0
        step = 1
    # Case where start and stop are provided, but step isn't
    elif step is None:
        step = 1

    # Initialize an empty list to store the range
    result = []

    # If step is positive, count up
    if step > 0:
        while start < stop:
            result.append(start)
            start += step
    # If step is negative, count down
    elif step < 0:
        while start > stop:
            result.append(start)
            start += step

    return result

# Test cases
print(myRange(15))
print(myRange(2, 30))
print(myRange(1, 10, 2))
print(myRange(10, 2, -1))