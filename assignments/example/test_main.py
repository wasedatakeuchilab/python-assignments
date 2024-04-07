import pytest

from main import print_hello


@pytest.mark.parametrize("n", [1, 2, 3, 5, 10])
def test_print_hello(n: int, capfd: pytest.CaptureFixture) -> None:
    print_hello(n)
    expect = "hello, world!\n" * n
    out, err = capfd.readouterr()
    assert out == expect
