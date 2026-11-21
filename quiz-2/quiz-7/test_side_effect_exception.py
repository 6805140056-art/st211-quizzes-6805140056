from unittest.mock import Mock
import pytest
def test_return_value():
    mock = Mock()
    mock.login.side_effect =RuntimeError(
       "Invalid credentials"
)
    with pytest.raises(ValueError):
       mock.login()
