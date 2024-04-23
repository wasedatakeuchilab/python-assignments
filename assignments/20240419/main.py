import functools


@functools.cache
def fibo(n: int) -> int:
    """Returns the n-th Fibonacci number."""
    if n < 0:
        raise ValueError('n is negative.')
    
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)