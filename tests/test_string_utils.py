from contextlib import nullcontext

import pytest

from src.string_utils import StringUtils


class TestStringUtils:

    @pytest.mark.parametrize(
        ("input_str", "expected"), [("sueta", "ateus"), ("", ""), ("123", "321")]
    )
    def test_reverse_string(self, input_str, expected):
        utils = StringUtils()
        assert utils.reverse_string(input_str) == expected

    @pytest.mark.parametrize(
        ("input_str", "expected"),
        [
            ("sueta", nullcontext()),
            (1234567, pytest.raises(TypeError)),
            (None, pytest.raises(TypeError)),
        ],
    )
    def test_reverse_string_errors(self, input_str, expected):
        utils = StringUtils()
        with expected:
            utils.reverse_string(input_str)

    @pytest.mark.parametrize(
        ("fullname", "expected"),
        [
            ("Daniil Nikolaev", "DN"),
            ("Ivan Ivanov", "II"),
            ("", pytest.raises(ValueError)),
        ],
    )
    def test_get_initials(self, fullname, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.get_initials(fullname) == expected
        else:
            with expected:
                utils.get_initials(fullname)
