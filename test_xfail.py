import pytest
@pytest.mark.xfail(reason="Known Bug #123, fix pending")
def test_known_broke_feature():
    assert 1 ==2
@pytest.mark.xfail(reason="Might pass sometimes")
def test_actually_work_now():
    assert 1 == 1