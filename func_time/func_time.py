"""Decorator to measure functions executing time"""

import time

def func_time(func):
    """Measures and prints the execution time of a function.

    This decorator wraps a function, records the time immediately before
    and after its execution, and prints the elapsed time in seconds.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"A function {func.__name__} executed in {elapsed:.4f} seconds")
    return wrapper
