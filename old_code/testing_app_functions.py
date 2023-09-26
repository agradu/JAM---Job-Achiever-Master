import pytest
from unittest import mock
from app_functions import input_strict, input_int, input_alfa, input_date, input_email


# Test input_strict function
def test_input_strict():
    user_input = mock.Mock(side_effect=["3", "2", "1"])
    with mock.patch("builtins.input", user_input):
        result = input_strict("Enter your choice: ", ["1", "2", "3"])
    assert result == "3"


# Test input_int function
def test_input_int():
    user_input = mock.Mock(side_effect=["abc", "123"])
    with mock.patch("builtins.input", user_input):
        result = input_int("Enter a number: ")
    assert result == 123


# Test input_alfa function
def test_input_alfa():
    user_input = mock.Mock(side_effect=["John Doe", "123", "Jane Smith"])
    with mock.patch("builtins.input", user_input):
        result = input_alfa("Enter your name: ")
    assert result == "John Doe"


# Test input_date function
def test_input_date():
    user_input = mock.Mock(side_effect=["2022-01-01", "01.01.2022"])
    with mock.patch("builtins.input", user_input):
        result = input_date("Enter a date (dd.mm.yyyy): ")
    assert result == "01.01.2022"


# Test input_email function
def test_input_email():
    user_input = mock.Mock(side_effect=["invalid_email", "test@example.com"])
    with mock.patch("builtins.input", user_input):
        result = input_email("Enter your email: ")
    assert result == "test@example.com"


# In these examples, the mock module is use to simulate user input for the input() function. I provided different inputs using the side_effect attribute of the mock.Mock object.
