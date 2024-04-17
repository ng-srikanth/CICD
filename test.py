import pytest

def addition(a, b):
    # Intentionally fail the function
    raise ValueError("Intentional function failure")

def test_addition():
    with pytest.raises(ValueError):
        addition(2, 2)