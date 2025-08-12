
import pytest


@pytest.mark.parametrize("a, b, c", [(1, 1, 2), (2, 2, 4), (3, 3, 6)])
def test_param(a, b, c):
    print(f"\n{a} + {b} = {c}")
    assert a + b == c
