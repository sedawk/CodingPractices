#!/usr/bin/python

import random
import unittest

def SmallestNumbers(numbers, count):
    subset = numbers[:count]
    for number in numbers[count:]:
        subset.sort(reverse=True)
        if subset[0] > number:
            subset[0] = number
    return subset


class TestCase(unittest.TestCase):
    def testFind3SmallestNumbers(self):
        numbers = random.sample(xrange(100), 10)
        actual = sorted(SmallestNumbers(numbers, 3))
        expected = sorted(numbers)[:3]
        assert expected == actual


if __name__ == "__main__":
    unittest.main()
