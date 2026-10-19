"""Utility functions for working with numbers."""

def is_positive_int(value):
    """True for ints greater than zero (bool is NOT accepted)."""
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def clamp(value, low, high):
    """Limit value to the range low..high."""
    return max(low, min(value, high))


def percent(part, whole):
    """part as a percentage of whole, rounded to 1 decimal; 0.0 if whole is 0."""
    if whole == 0:
        return 0.0
    return round(part / whole * 100, 1)