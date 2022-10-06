from calculator import *

# See if correctly formed strings are detected
def testCorrectStrings():
    input = "1+2"
    result = verifyString(input)
    assert result == "1+2"

    input = "46+23"
    result = verifyString(input)
    assert result == "46+23"

    input = "45-34+24632*478"
    result = verifyString(input)
    assert result == "45-34+24632*478"

# See if malformed strings are detected
def testMalformedStrings():
    input = "1+s2"
    result = verifyString(input)
    assert result == "Error: Unknown/Disallowed character: s"

    input = "4-*47"
    result = verifyString(input)
    assert result == "Error: Duplicate operation: -*"

    input = "3+8-"
    result = verifyString(input)
    assert result == "Error: Ended on an operator: -"

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
    
# Test if evaluate can handle addition with multiple arguments
def testAddition():
    input = "45+23+101"
    expected = 169
    result = evaluate(input)
    assert expected == result

    input = "5+300+20"
    expected = 325
    result = evaluate(input)
    assert expected == result

# Test evaluate with multiple arguments
def testEvaluate():
    input = "45+23-101*2"
    expected = -134
    result = evaluate(input)
    assert expected == result

    input = "5+300*0"
    expected = 5
    result = evaluate(input)
    assert expected == result

    input = "5*12-6"
    expected = 54
    result = evaluate(input)
    assert expected == result

    input = "100*10-100"
    expected = 900
    result = evaluate(input)
    assert expected == result

    input = "10*10*8"
    expected = 800
    result = evaluate(input)
    assert expected == result