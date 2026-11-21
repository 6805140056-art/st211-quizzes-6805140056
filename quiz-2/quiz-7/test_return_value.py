from unittest.mock import Mock
def test_return_value():
  mock = Mock()
  mock.get_status.return_value = "123"
  assert mock.get_status() == "OK"
  print(mock.get_status())
  print(mock.get_status())
  print(mock.get_status())