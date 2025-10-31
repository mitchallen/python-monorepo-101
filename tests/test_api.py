"""Tests for the api package."""

from api.services import PaymentService, UserService


def test_payment_service():
    """Test payment service."""
    service = PaymentService()
    result = service.calculate_total(100, 0.1)
    assert result == "USD $110.00"


def test_user_service():
    """Test user service."""
    service = UserService()
    result = service.validate_user("test@example.com", "555-1234")
    assert result["email_valid"] is True
    assert result["phone_valid"] is True

    invalid_result = service.validate_user("invalid-email", "invalid-phone")
    assert invalid_result["email_valid"] is False
    assert invalid_result["phone_valid"] is False
