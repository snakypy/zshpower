from functools import wraps


def assign_cli(arguments, command):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if arguments[command]:
                return func(*args, **kwargs)

        return wrapper

    return decorator


def runtime(func):
    """Decorator to test runtime others functions.

    Returns:
        str: Return print
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        from datetime import datetime

        start_time = datetime.now()
        context = func(*args, **kwargs)
        print(f"Time taken: {datetime.now() - start_time}")
        return context

    return wrapper


def silent_errors(func):
    from contextlib import suppress

    @wraps(func)
    def wrapper(*args, **kwargs):
        with suppress(NameError, TypeError, KeyboardInterrupt):
            return func(*args, **kwargs)
    return wrapper
