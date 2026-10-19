"""Utility functions for working with strings."""

def normalize_whitespace(text):
    """Trim the text and collapse runs of whitespace into one space."""
    return " ".join(text.split())


def slugify(text):
    """'  Login Page: Happy Path ' -> 'login-page-happy-path'."""
    cleaned = normalize_whitespace(text).lower()
    kept = [ch if ch.isalnum() else " " for ch in cleaned]
    return "-".join("".join(kept).split())


def is_valid_email(email):
    """True when email has exactly one '@' and a '.' in the domain part."""
    return email.count("@") == 1 and "." in email.split("@")[1]

def mask_email(email):
    """Mask the email address, keeping the first character and domain visible."""
    if not is_valid_email(email):
        return email  # Return as is if not a valid email
    local_part, domain = email.split("@")
    return local_part[0] + "***@" + domain