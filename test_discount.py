import pytest
from discount import apply_discount
@pytest.mark.parametrize("price, present,expected",[
    (100,0,100),
    (100,50,50),
    (100,100,0),
    (200,25,150),
    (80, 10, 72),
])
def test_discount_calculation(price,present,expected):
    assert apply_discount(price,present) == expected
