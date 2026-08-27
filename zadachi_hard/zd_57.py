import pytest
from datetime import datetime

@pytest.fixture
def timer():
    return datetime.now()

def test_example(timer):
    time_start = timer
    assert 2 + 2 == 4
    end = timer
    print("Время выполнения теста:", end - time_start)