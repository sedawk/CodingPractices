#!/usr/bin/python

import random

def FindSetsOfNumbers(numbers, total):
    subset = []
    helper(numbers, subset, 0, total)

def helper(numbers, subset, index, total):
    if total == 0:
        print []
    elif index == len(numbers):
        return
    elif total == sum(subset):
        print subset
    else:
        # Subset not including the current number
        helper(numbers, subset, index + 1, total)
        # Subset including the current number
        newSubset = list(subset)
        newSubset.append(numbers[index])
        helper(numbers, newSubset, index + 1, total)

if __name__ == "__main__":
    numbers = random.sample(xrange(20), 10)
    print numbers
    FindSetsOfNumbers(numbers, 16)
