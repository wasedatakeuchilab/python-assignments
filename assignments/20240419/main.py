import functools


@functools.cache
def fibo(n: int) -> int:
    """Returns the n-th Fibonacci number."""
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)
