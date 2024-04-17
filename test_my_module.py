# test_addition.py

import pytest
from addition import add

def test_addition_positive_numbers():
    assert add(3, 5) == 8

def test_addition_negative_numbers():
    assert add(-3, -5) == -8

def test_addition_mixed_numbers():
    assert add(3, -5) == -2

def test_addition_zero():
    assert add(3, 0) == 2
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_addition_float():
    assert add(3.5, 2.5) == 6.0

# Additional test cases can be added as needed
