import pytest
from calculator import add, division

def test_add_two_numbers():
    assert add(5, 5) == 10
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(1, 0) == 1

def test_subtract():
    from calculator import subtract
    assert subtract(10, 3) == 7

def test_divide():
    assert division(8, 2) == 4
    assert division(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(5, 0)