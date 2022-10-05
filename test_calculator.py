from calculator import *

# See if correctly formed strings are detected
def testCorrectStrings():
    expected = True

    input = "1+2"
    result = verifyString(input)
    assert expected == result

    input = "46+23"
    result = verifyString(input)
    assert expected == result

    input = "45-34+24632*478"
    result = verifyString(input)
    assert expected == result

# See if malformed strings are detected
def testMalformedStrings():
    expected = False

    input = "1+s2"
    result = verifyString(input)
    assert expected == result

    input = "4-*47"
    result = verifyString(input)
    assert expected == result

    input = "3+8-"
    result = verifyString(input)
    assert expected == result

# Test if precedence is correctly handled
def testPrecedence():
    input = "+"
    expected = 1
    result = precedence(input)
    assert expected == result

    input = "-"
    expected = 1
    result = precedence(input)
    assert expected == result

    input = "*"
    expected = 2
    result = precedence(input)
    assert expected == result

# Test if subCalc can multiply
def testSubCalcMultiplication():
    expected = 108
    result = sub_calc(12, 9, '*')
    assert expected == result

    expected = 21
    result = sub_calc(3, 7, '*')
    assert expected == result

    expected = 0
    result = sub_calc(483, 0, '*')
    assert expected == result

    expected = 1
    result = sub_calc(1, 1, '*')
    assert expected == result
    
# Test if subCalc can add
def testSubCalcAddition():
    expected = 9
    result = sub_calc(9, 0, '+')
    assert expected == result

    expected = 32
    result = sub_calc(5, 27, '+')
    assert expected == result

    expected = 0
    result = sub_calc(0, 0, '+')
    assert expected == result

# Test if subCalc can subtract
def testSubCalcSubtraction():
    expected = 9
    result = sub_calc(9, 0, '-')
    assert expected == result

    expected = 21
    result = sub_calc(26, 5, '-')
    assert expected == result

    expected = -5
    result = sub_calc(5, 10, '-')
    assert expected == result

# Test digit appender for converting strings to integers
def testAppendDigits():
    expected = 123
    i = 0
    inputString = "123"
    values = []
    i, inputString, values = appendDigits(i, inputString, values)
    assert expected == values[0]

    expected = 491
    i = 0
    inputString = "491"
    values = []
    i, inputString, values = appendDigits(i, inputString, values)
    assert expected == values[0]

    expected = 7516
    i = 0
    inputString = "7516"
    values = []
    i, inputString, values = appendDigits(i, inputString, values)
    assert expected == values[0]

