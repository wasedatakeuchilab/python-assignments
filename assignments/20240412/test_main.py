import pytest

from main import fizzbuzz

FIZZBUZZ = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
    "16",
    "17",
    "Fizz",
    "19",
    "Buzz",
    "Fizz",
    "22",
    "23",
    "Fizz",
    "Buzz",
    "26",
    "Fizz",
    "28",
    "29",
    "FizzBuzz",
]


@pytest.mark.parametrize("n", [1, 3, 5, 15, 21, 25, 30])
def test_fizzbuzz(n: int, capfd: pytest.CaptureFixture) -> None:
    fizzbuzz(n)
    expect = "\n".join(FIZZBUZZ[:n]) + "\n"
    out, err = capfd.readouterr()
    assert out == expect
