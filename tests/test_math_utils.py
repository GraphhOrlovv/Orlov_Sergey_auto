import allure
import pytest

from src.math_utils import Math_Operations

pytestmark = [
    allure.parent_suite("Тестирование собственных функций"),
    allure.suite("Тестирование работы калькулятора"),
]


@allure.epic("Проверка калькулятора")
@allure.title("Деление двух чисел")
@pytest.mark.parametrize(("a", "b", "expected"), [(1, 2, 0.5), (3, 3, 1), (10, 5, 2)])
def test_divide(a, b, expected):
    with allure.step(f"Проверяем число {a} и число {b}"):
        utils = Math_Operations()
        assert utils.divide(a, b) == expected
