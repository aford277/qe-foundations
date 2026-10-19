"""Utility functions for working with dates."""
from datetime import datetime, timedelta

def add_days(day, days):
    """Return the date `days` after `day` (a datetime.date). Negative goes back."""
    return day + timedelta(days=days)


def is_weekend(day):
    """True when the date falls on Saturday or Sunday."""
    return day.weekday() >= 5


def timestamp_for_filename(moment=None):
    """'20250131_093000' - safe to use inside file and folder names."""
    moment = moment or datetime.now()
    return moment.strftime("%Y%m%d_%H%M%S")

def days_between(start, end):
    """Return the number of whole days between two dates (end - start)."""
    return (end - start).days