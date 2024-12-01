import pytest
from calculator.CalculatorLogic import CalculatorLogic

# Tests for operations functions
def test_addition():
    calc = CalculatorLogic()
    result = calc.add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"

def test_subtraction():
    calc = CalculatorLogic()
    result = calc.subtract(5, 3)
    assert result == 2, f"Expected 2, but got {result}"

def test_multiplication():
    calc = CalculatorLogic()
    result = calc.multiply(4, 3)
    assert result == 12, f"Expected 12, but got {result}"

def test_division():
    calc = CalculatorLogic()
    result = calc.divide(6, -2)
    assert result == -3, f"Expected -3, but got {result}"

def test_division_by_zero():
    calc = CalculatorLogic()
    result = calc.divide(6, 0)
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"


# Tests for the syntax verification function
def test_syntax_valid():
    calc = CalculatorLogic()
    calc.calcul = ["2", "+", "3"]
    assert calc.verify_syntax() is True

def test_syntax_invalid_operator():
    calc = CalculatorLogic()
    calc.calcul = ["2", "%", "3"]
    assert calc.verify_syntax() is False

def test_syntax_missing_values():
    calc = CalculatorLogic()
    calc.calcul = ["", "+", "3"]
    assert calc.verify_syntax() is False

def test_syntax_invalid_values():
    calc = CalculatorLogic()
    calc.calcul = ["two", "+", "3"]
    assert calc.verify_syntax() is False



# Tests for result calculation
def test_calcul_addition():
    calc = CalculatorLogic()
    calc.calcul = ["2", "+", "3"]
    result = calc.calculate_result()
    assert result == 5, f"Expected 5, but got {result}"

def test_calcul_subtraction():
    calc = CalculatorLogic()
    calc.calcul = ["5", "-", "3"]
    result = calc.calculate_result()
    assert result == 2, f"Expected 2, but got {result}"

def test_calcul_multiplication():
    calc = CalculatorLogic()
    calc.calcul = ["4", "*", "3"]
    result = calc.calculate_result()
    assert result == 12, f"Expected 12, but got {result}"

def test_calcul_division():
    calc = CalculatorLogic()
    calc.calcul = ["6", "/", "-2"]
    result = calc.calculate_result()
    assert result == -3, f"Expected 3, but got {result}"

def test_calcul_division_by_zero():
    calc = CalculatorLogic()
    calc.calcul = ["6", "/", "0"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"

def test_calcul_empty_values():
    calc = CalculatorLogic()
    calc.calcul = ["", "+", "3"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"

def test_calcul_missing_operator():
    calc = CalculatorLogic()
    calc.calcul = ["2", "", "3"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"

def test_calcul_invalid_operator():
    calc = CalculatorLogic()
    calc.calcul = ["2", "%", "3"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"

def test_calcul_invalid_number():
    calc = CalculatorLogic()
    calc.calcul = ["two", "+", "3"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"

def test_calcul_valid_numbers_but_invalid_operator():
    calc = CalculatorLogic()
    calc.calcul = ["2", "*", "three"]
    result = calc.calculate_result()
    assert result == "Syntax error", f"Expected 'Syntax error', but got {result}"