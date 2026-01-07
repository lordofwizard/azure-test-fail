import pytest
from main import (
    add, subtract, multiply, divide, power,
    is_even, is_positive, factorial, reverse_string, count_vowels
)


# Test cases for add function
def test_add_positive_numbers():
    assert add(5, 3) == 8


def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_add_mixed_numbers():
    assert add(10, -5) == 5


def test_add_zero():
    assert add(0, 5) == 5


# Test cases for subtract function
def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_to_zero():
    assert subtract(5, 5) == 0


def test_subtract_negative_result():
    assert subtract(3, 10) == -7


# Test cases for multiply function
def test_multiply_positive_numbers():
    assert multiply(4, 5) == 20


def test_multiply_negative_numbers():
    assert multiply(-4, -5) == 20


def test_multiply_by_zero():
    assert multiply(100, 0) == 0


def test_multiply_mixed_signs():
    assert multiply(-4, 5) == -20


# Test cases for divide function
def test_divide_positive_numbers():
    assert divide(10, 2) == 5


def test_divide_negative_numbers():
    assert divide(-10, -2) == 5


def test_divide_mixed_signs():
    assert divide(-10, 2) == -5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)


# Test cases for power function
def test_power_positive_exponent():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_power_fractional():
    assert power(4, 0.5) == 2.0


# Test cases for is_even function
def test_is_even_even_number():
    assert is_even(4) == True


def test_is_even_odd_number():
    assert is_even(7) == False


def test_is_even_zero():
    assert is_even(0) == True


def test_is_even_negative_even():
    assert is_even(-6) == True


# Test cases for is_positive function
def test_is_positive_positive_number():
    assert is_positive(10) == True


def test_is_positive_negative_number():
    assert is_positive(-10) == False


def test_is_positive_zero():
    assert is_positive(0) == False


def test_is_positive_float():
    assert is_positive(3.14) == True


# Test cases for factorial function
def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_negative_raises_error():
    with pytest.raises(ValueError):
        factorial(-5)


# Test cases for reverse_string function
def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_single_char():
    assert reverse_string("a") == "a"


def test_reverse_string_palindrome():
    assert reverse_string("racecar") == "racecar"


# Test cases for count_vowels function
def test_count_vowels_all_vowels():
    assert count_vowels("aeiou") == 5


def test_count_vowels_no_vowels():
    assert count_vowels("xyz") == 0


def test_count_vowels_mixed():
    assert count_vowels("hello world") == 3


def test_count_vowels_uppercase():
    assert count_vowels("HELLO") == 2


# Test division with float result - using pytest.approx for tolerance
def test_divide_type_error():
    result = divide(10, 3)
    assert result == pytest.approx(3.333, rel=1e-2)  # Fixed: Use pytest.approx for float comparison
