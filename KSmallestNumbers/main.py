#!/usr/bin/python

import random

def SmallestNumbers(numbers, count):
    subset = numbers[:count]
    for number in numbers[count:]:
        subset.sort(reverse=True)
        if subset[0] > number:
            subset[0] = number
    return subset

if __name__ == "__main__":
    numbers = random.sample(xrange(100), 10)
    print numbers
    print SmallestNumbers(numbers, 3)
