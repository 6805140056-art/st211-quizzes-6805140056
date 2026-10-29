import pytest
from discount import apply_discount
@pytest.mark.parametrize("bad_present",[-1,-50,101,200])
def test_invalid_present_raises(bad_present):
    with pytest.raises(ValueError):
        apply_discount(100,bad_present)
