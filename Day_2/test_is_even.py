'''
Pytest Challenge: Create a test function using pytest.mark.parametrize 
that checks if a function is_even(n) returns True for 2, 4, 6 and False for 1, 3, 5.
'''
import pytest

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
@pytest.mark.parametrize(("number","expected"),[(1,False),(2,True),(3,False),(4,True),(5,False),(6,True)])
def test_is_even(number,expected):
    assert is_even(number) == expected