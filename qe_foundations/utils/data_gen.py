"""Utility functions for generating test data."""
import random

FIRST_NAMES = ["Asha", "Ben", "Carla", "Dev", "Elena", "Farid"]
ROLES = ["viewer", "editor", "admin"]


def make_users(count, seed=None):
    """Return `count` user dicts. The same seed always gives the same users."""
    rng = random.Random(seed)
    users = []
    for i in range(1, count + 1):
        name = rng.choice(FIRST_NAMES)
        users.append({
            "id": i,
            "name": name,
            "email": f"{name.lower()}{i}@example.com",
            "age": rng.randint(18, 65),
            "role": rng.choice(ROLES),
        })
    return users