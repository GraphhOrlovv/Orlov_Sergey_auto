from src.math_utils import Math_Operations

import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 0.5),
        (3, 3, 1),
        (10, 5, 2)
    ]
)
def test_divide(a, b, expected):
    utils = Math_Operations()
    assert utils.divide(a, b) == expected
