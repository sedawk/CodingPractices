#!/usr/bin/python

import unittest

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(func):
    def first(a, b):
        return a
    return func(first)

def cdr(func):
    def second(a, b):
        return b
    return func(second)


class TestCase(unittest.TestCase):
    def testA(self):
        assert 3 == car(cons(3, 4))

    def testB(self):
        assert 4 == cdr(cons(3, 4))
    

if __name__ == "__main__":
    unittest.main()
    
