"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# ------------------------------------------------------------------------------
# A most basic test fuction
# ------------------------------------------------------------------------------


def test_one_plus_one():
    """This test will pass."""
    assert 1 + 1 == 2

def test_one_plus_two():
    """This test will fail."""
    a = 1
    b = 2
    c = 0
    assert a + b == c
