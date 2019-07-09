#!/usr/bin/python

import unittest

def ProductOfAllNumbers(numbers):
    products = [reduce((lambda x, y: x * y), numbers)] * len(numbers)
    return [x / y for x, y in zip(products, numbers)]

class TestCase(unittest.TestCase):
    def testA(self):
        numbers = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        actual = ProductOfAllNumbers(numbers)
        assert expected == actual, actual

    def testB(self):
        numbers = [3, 2, 1]
        expected = [2, 3, 6]
        actual = ProductOfAllNumbers(numbers)
        assert expected == actual, actual

if __name__ == "__main__":
    unittest.main()
    
