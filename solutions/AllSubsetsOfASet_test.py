#!/usr/bin/python

import unittest


def all_subsets(given_array):
    subset = [None] * len(given_array)
    result = []
    helper(given_array, subset, 0, result)
    return result

def helper(given_array, subset, index, result):
    if index == len(given_array):
        result.append(list(subset))
    else:
        subset[index] = None
        helper(given_array, subset, index + 1, result)
        subset[index] = given_array[index]
        helper(given_array, subset, index + 1, result)

class TestCase(unittest.TestCase):
    def testPopulateAllSubsets(self):
        expected = [
            [None, None, None, None],
            [None, None, None, 4],
            [None, None, 3, None],
            [None, None, 3, 4],
            [None, 2, None, None],
            [None, 2, None, 4],
            [None, 2, 3, None],
            [None, 2, 3, 4],
            [1, None, None, None],
            [1, None, None, 4],
            [1, None, 3, None],
            [1, None, 3, 4],
            [1, 2, None, None],
            [1, 2, None, 4],
            [1, 2, 3, None],
            [1, 2, 3, 4],
        ]
        
        numbers = range(1, 5)
        actual = all_subsets(numbers)
        diff = [subset for subset in expected if subset not in actual]
        assert 0 == len(diff)
        
if __name__ == "__main__":
    unittest.main()
