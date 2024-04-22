import functools


@functools.cache
def fibo(n: int) -> int:
    """Returns the n-th Fibonacci number."""
