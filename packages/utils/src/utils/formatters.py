"""Formatting utilities."""


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a number as currency."""
    return f"{currency} ${amount:,.2f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Format a number as a percentage."""
    return f"{value * 100:.{decimals}f}%"
