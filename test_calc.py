import calc
import pytest

def test_add():
    assert calc.add(10, 5) == 15

def test_subtract():
    assert calc.subtract(10, 5) == 5