"""Example API services demonstrating package dependencies."""

from core.calculator import Calculator
from utils.formatters import format_currency
from utils.validators import validate_email, validate_phone


class PaymentService:
    """Service for handling payment calculations."""

    def __init__(self):
        self.calc = Calculator()

    def calculate_total(self, subtotal: float, tax_rate: float) -> str:
        """Calculate total with tax and return formatted currency."""
        tax = self.calc.multiply(subtotal, tax_rate)
        total = self.calc.add(subtotal, tax)
        return format_currency(total)


class UserService:
    """Service for user validation."""

    def validate_user(self, email: str, phone: str) -> dict[str, bool]:
        """Validate user email and phone."""
        return {
            "email_valid": validate_email(email),
            "phone_valid": validate_phone(phone),
        }
