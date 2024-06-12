import pytest
from app.functions import divide, hello_world, add


@pytest.mark.parametrize(
    "x, y, result",
    [(-5, 2, -2.5), (5, 5, 1), (100, 10, 10)],
)
def test_divide_success(x, y, result):
    assert divide(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [(5, 8, 4), (5, 5, 2), (-37, 15, 4)],
)
def test_divide_fail(x, y, result):
    assert divide(x, y) != result


def test_divide_exception():
    with pytest.raises(ZeroDivisionError):
        divide(13, 0)


@pytest.mark.parametrize(
    "x, y, result",
    [(4, 2, 6), (-5, 5, 0), (100, -10, 90)],
)
def test_add_success(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [(6, 8, -5), (14, 5, 8), (-35, -55, 0)],
)
def test_add_fail(x, y, result):
    assert add(x, y) != result


def test_hello_world(capsys):
    hello_world()
    out, _ = capsys.readouterr()
    assert out == "Hello, world!\n"
