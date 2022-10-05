import unittest
from calculator import *

class Testing(unittest.TestCase):
    # Test if precedence is correctly handled
    def testPrecedence(self):
        input = "+"
        expected = 1
        result = precedence(input)
        self.assertEqual(expected, result)

        input = "-"
        expected = 1
        result = precedence(input)
        self.assertEqual(expected, result)

        input = "*"
        expected = 2
        result = precedence(input)
        self.assertEqual(expected, result)

    # Test if subCalc can multiply
    def testSubCalcMultiplication(self):
        expected = 108
        result = sub_calc(12, 9, '*')
        self.assertEqual(expected, result)

        expected = 21
        result = sub_calc(3, 7, '*')
        self.assertEqual(expected, result)

        expected = 0
        result = sub_calc(483, 0, '*')
        self.assertEqual(expected, result)

        expected = 1
        result = sub_calc(1, 1, '*')
        self.assertEqual(expected, result)
        
    # Test if subCalc can add
    def testSubCalcAddition(self):
        expected = 9
        result = sub_calc(9, 0, '+')
        self.assertEqual(expected, result)

        expected = 32
        result = sub_calc(5, 27, '+')
        self.assertEqual(expected, result)

        expected = 0
        result = sub_calc(0, 0, '+')
        self.assertEqual(expected, result)

    # Test if subCalc can subtract
    def testSubCalcSubtraction(self):
        expected = 9
        result = sub_calc(9, 0, '-')
        self.assertEqual(expected, result)

        expected = 21
        result = sub_calc(26, 5, '-')
        self.assertEqual(expected, result)

        expected = -5
        result = sub_calc(5, 10, '-')
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()