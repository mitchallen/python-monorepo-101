"""Tests for the utils package."""

from utils.formatters import format_currency, format_percentage
from utils.validators import validate_email, validate_phone


def test_format_currency():
    """Test currency formatting."""
    assert format_currency(1234.56) == "USD $1,234.56"
    assert format_currency(100, "EUR") == "EUR $100.00"


def test_format_percentage():
    """Test percentage formatting."""
    assert format_percentage(0.1234) == "12.34%"
    assert format_percentage(0.5, 0) == "50%"


def test_validate_email():
    """Test email validation."""
    assert validate_email("test@example.com") is True
    assert validate_email("invalid-email") is False
    assert validate_email("user.name@domain.co.uk") is True


def test_validate_phone():
    """Test phone validation."""
    assert validate_phone("555-1234") is True
    assert validate_phone("(555) 123-4567") is True
    assert validate_phone("555.123.4567") is True
    assert validate_phone("invalid") is False
