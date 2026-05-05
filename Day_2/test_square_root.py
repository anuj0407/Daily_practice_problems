'''
Exception Challenge: Write a test that ensures a ValueError is raised
when passing a negative number to a function called square_root(n).
'''
import pytest

def square_root(n):
    if n<0:
        raise ValueError
    return n**(1/2)

#test
@pytest.mark.parametrize("number",[-4,-9,-16])
def test_square_root(number):
    with pytest.raises(ValueError):
        square_root(number)