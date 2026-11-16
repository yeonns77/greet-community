"""A small greeting package with a contributing guide."""


def greet(name: str) -> str:
    """Return a greeting for name, using world when name is blank."""
    return f"Hello, {name.strip() or 'world'}!"
