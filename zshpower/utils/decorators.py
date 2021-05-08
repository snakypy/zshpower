from contextlib import suppress
from datetime import datetime
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


def runtime(func: Any):
    """Decorator to test runtime others functions.

    Returns:
        str: Return print
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        context = func(*args, **kwargs)
        print(f"Time taken: {datetime.now() - start_time}")
        return context

    return wrapper


def silent_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with suppress(NameError, TypeError, KeyboardInterrupt):
            return func(*args, **kwargs)

    return wrapper


# def invisible_cursor(func):
#     import curses
#     from time import sleep
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         curses.initscr()
#         curses.curs_set(0)
#         f = func(*args, **kwargs)
#         curses.curs_set(1)
#         curses.endwin()
#         return f
#     return wrapper
