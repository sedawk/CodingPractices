#!/usr/bin/python

import unittest

def MaxValuesOfSubArrays(numbers, k):
    result = []
    for i in range(0, len(numbers) - k + 1):
        result.append(max(numbers[i: i + k]))
    return result

class TestCase(unittest.TestCase):
    def testMaxValues(self):
        numbers = [10, 5, 2, 7, 8, 7]
        expected = [10, 7, 8, 8]
        actual = MaxValuesOfSubArrays(numbers, 3)
        assert expected == actual

if __name__ == "__main__":
    unittest.main()
