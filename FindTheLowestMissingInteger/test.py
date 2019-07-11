#!/usr/bin/python

import unittest

def FindLowestMissingNumber(numbers):
    a = min(numbers)
    b = max(numbers) + 1
    allNumbers = range(a, b)
    diff = [number for number in allNumbers if number not in numbers and number > 0]
    return b if len(diff) == 0 else diff[0]


class TestCase(unittest.TestCase):
    def test1(self):
        numbers = [3, 4, -1, 1]
        assert 2 == FindLowestMissingNumber(numbers)

    def test2(self):
        numbers = [1, 2, 0]
        assert 3 == FindLowestMissingNumber(numbers)

if __name__ == "__main__":
    unittest.main()
