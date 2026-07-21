from src.math_utils import Math_Operations

import pytest

def test_divide():
    utils = Math_Operations()
    assert utils.divide(5 ,3)