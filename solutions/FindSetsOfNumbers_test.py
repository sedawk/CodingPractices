#!/usr/bin/python

import unittest
import random

def FindSetsOfNumbers(numbers, total):
    subset = []
    collected = []
    helper(numbers, subset, 0, total, collected)
    return collected

def helper(numbers, subset, index, total, collected):
    if total == 0:
        return
    elif index == len(numbers):
        return
    elif total == sum(subset):
        collected.append(subset)
    else:
        # Subset not including the current number
        helper(numbers, subset, index + 1, total, collected)
        # Subset including the current number
        newSubset = list(subset)
        newSubset.append(numbers[index])
        helper(numbers, newSubset, index + 1, total, collected)

        
class TestCase(unittest.TestCase):
    def testIfSumOfEachGroupIs16(self):
        numbers = random.sample(xrange(20), 10)
        groups = FindSetsOfNumbers(numbers, 16)
        for group in groups:
            assert 16 == sum(group)

    
if __name__ == "__main__":
    unittest.main()
