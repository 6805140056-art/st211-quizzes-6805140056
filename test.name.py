from dataclasses import dataclass

import  pytest
from bank import BankAccount
def test_deposit_positive_amount_increase_balance():
    account =BankAccount(100)
    account.deposit(50)
    assert  account.balance ==150
def test_deposit_negative_amount_raises_value():
   account =BankAccount(100)
   with pytest.raises(ValueError):
       account.deposit(-10)
def test_withdraw_more_than_balance_raises_value_error():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(200)

