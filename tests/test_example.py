#!/usr/bin/env python3
"""
Example test file
"""
import unittest

class TestExample(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(2 + 2, 4)
        
    def test_string(self):
        self.assertEqual("hello".upper(), "HELLO")

if __name__ == "__main__":
    unittest.main()
