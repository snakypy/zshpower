from functools import wraps


def assign_cli(arguments: dict, command: str):
    """
    Decorator that takes several parameters to assign to the ZSHPower CLI commands.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[command]:
                return func(*args, **kwargs)

        return wrapper

    return decorator
