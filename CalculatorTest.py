import pytest
from Calculator import Calculator
from collections import deque


@pytest.fixture(scope='module')
def c():
    return Calculator()


def test_process_add_minus_1(c):
    result = c.process_add_minus(deque([1, '+', 3]))
    assert result.pop() == 4


def test_process_add_minus_2(c):
    result = c.process_add_minus(deque([3, '-', 1]))
    assert result.pop() == 2


def test_process_times_divided1(c):
    result = c.process_times_divided(deque([2, '*', 3]))
    assert result.pop() == 6


def test_process_times_divided2(c):
    result = c.process_times_divided(deque([9, '/', 3]))
    assert result.pop() == 3


def test_add(c):
    result = c.cal('1+2+3+4+15')
    assert result == 25


def test_minus(c):
    result = c.cal('100-5-6-7-8-9')
    assert result == 65


def test_times(c):
    result = c.cal('1*2*3*4')
    assert result == 24


def test_divided(c):
    result = c.cal('100/2/5/2')
    assert result == 5


def test_arithmetic1(c):
    result = c.cal('100/2/5*2')
    assert result == 20


def test_arithmetic2(c):
    result = c.cal('5+3*4-9/3')
    assert result == 14
