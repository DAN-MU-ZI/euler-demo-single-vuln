"""User lookup helper added in a feature pull request."""

import sqlite3


def find_user_by_name(conn: sqlite3.Connection, username: str):
    """Query a user record using unsanitized string interpolation."""
    query = f"SELECT id, username FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchall()
