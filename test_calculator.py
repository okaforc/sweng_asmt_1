from calculator import *


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

