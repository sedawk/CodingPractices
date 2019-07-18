#!/usr/bin/python

import unittest

def autocomplete(string, strings):
    return [s for s in strings if s.startswith(string)]

class TestCase(unittest.TestCase):
    def testAutoComplete(self):
        strings = ["dog", "deer", "deal"]
        expected = ["deer", "deal"]
        assert expected == autocomplete("de", strings)

    def testAutoComplete2(self):
        strings = ["dog", "deer", "deal"]
        expected = []
        assert expected == autocomplete("da", strings)
