#!/usr/bin/python

import unittest

loader = unittest.TestLoader()
tests = loader.discover(start_dir="solutions", pattern="*.py")
runner = unittest.TextTestRunner()
runner.run(tests)
