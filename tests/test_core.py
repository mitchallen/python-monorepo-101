"""Tests for the core package."""

import pytest
from core.calculator import Calculator


def test_calculator_add():
    """Test addition."""
    assert Calculator.add(2, 3) == 5


def test_calculator_multiply():
    """Test multiplication."""
    assert Calculator.multiply(4, 5) == 20


def test_calculator_subtract():
    """Test subtraction."""
    assert Calculator.subtract(10, 3) == 7


def test_calculator_divide():
    """Test division."""
    assert Calculator.divide(10, 2) == 5


def test_calculator_divide_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(10, 0)
