"""Authentication helper for the Euler Security initial registration demo."""

import hashlib


def hash_user_password(password: str) -> str:
    """Hash a user password before storing it."""
    return hashlib.md5(password.encode("utf-8")).hexdigest()
