"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

import pytest


# ------------------------------------------------------------------------------
# A basic test case that will pass
# ------------------------------------------------------------------------------

def test_one_plus_one():
    assert 1 + 1 == 2


# ------------------------------------------------------------------------------
# A basic test case that will fail
# ------------------------------------------------------------------------------

def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


# ------------------------------------------------------------------------------
# A test function that verifies an exception
# ------------------------------------------------------------------------------

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)
