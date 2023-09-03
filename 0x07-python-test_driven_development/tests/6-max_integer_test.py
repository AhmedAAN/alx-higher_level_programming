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

    def testMaxAtTheBeginning(self):
        '''Test a list with the max value at the beginning'''
        beginning = [4, 1, 2, 3]
        self.assertEqual(max_integer(beginning), 4) 

    def testEmptyList(self):
        '''Test an empty list'''
        empty = []
        self.assertEqual(max_integer(empty), None)

    def testOneElement(self):
        '''Test a one element list'''
        oneElement = [7]
        self.assertEqual(max_integer(oneElement), 7)

    def testFloats(self):
        '''Test a float list'''
        floats = [2.5, 1.7, -1.8, 8.9]
        self.assertEqual(max_integer(floats), 8.9)

    def testFloatsAndIntegers(self):
        '''Test a floats and integers list'''
        floatsAndIntegers = [1, 2, -7, 9.2]
        self.assertEqual(max_integer(floatsAndIntegers), 9.2)

    def testString(self):
        '''Test a string'''
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')

    def testListOfStrings(self):
        '''Test list of strings'''
        listString = ["Hello", "World", "Good", "People"]
        self.assertEqual(max_integer(listString), "World")

    def testEmptyString(self):
        '''Test an empty string'''
        emptyString = ""
        self.assertEqual(max_integer(emptyString), None)
        
if __name__ == '__main__':
    unittest.main()