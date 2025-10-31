"""Validation utilities."""

import re


def validate_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate phone number format (basic US format)."""
    # Remove all non-digit characters for validation
    digits_only = re.sub(r"\D", "", phone)
    # Accept 7 digits (local) or 10-11 digits (with/without country code)
    return 7 <= len(digits_only) <= 11
