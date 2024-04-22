import pytest

from main import fibo

FIBONACCI_SEQUENCE = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    10: 55,
    20: 6765,
    30: 832040,
    50: 12586269025,
}


@pytest.mark.parametrize("n", list(FIBONACCI_SEQUENCE.keys()))
def test_fibo(n: int) -> None:
    actual = fibo(n)
    expect = FIBONACCI_SEQUENCE[n]
    assert actual == expect


@pytest.mark.parametrize("n", [-1, -3, -10])
def test_fibo_with_negative_number(n: int) -> None:
    with pytest.raises(ValueError):
        fibo(n)
