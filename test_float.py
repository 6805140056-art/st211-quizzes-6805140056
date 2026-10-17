from pytest import  approx
def test_float():
    assert  0.1 + 0.2 == approx(0.3)
def test_float_without_appro_fails():
    assert  0.1 + 0.2 != 0.3
    