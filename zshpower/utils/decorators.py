from functools import wraps
from typing import Any


def assign_cli(arguments: dict, command: str) -> Any:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[command]:
                return func(*args, **kwargs)

        return wrapper

    return decorator
