#!/usr/bin/python3
'''Unittests for max_integer'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Define unittests for max integer'''

    def testOrderedList(self):
        '''Test an ordered list of integers'''
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def testUnorderdList(self):
        '''Test an unordered list of integers'''
        unorderd = [1, 5, 3, -6]
        self.assertEqual(max_integer(unorderd), 5)

if __name__ == '__main__':
    unittest.main()