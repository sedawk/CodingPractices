#!/usr/bin/python

import pickle
import unittest

def serialize(node):
    return pickle.dumps(node)

def deserialize(node):
    return pickle.loads(node)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class TestCase(unittest.TestCase):
    def testSerialize(self):
        node = Node("root", Node("left", Node("left.left")), Node("right"))
        assert deserialize(serialize(node)).left.left.val == "left.left"
        
if __name__ == "__main__":
    unittest.main()
