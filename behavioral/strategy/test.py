import pytest

from main import Client
from strategy import Strategy, StrategyAdd, StrategyMultiply


def test_add():
    strategy: Strategy = StrategyAdd()
    client = Client(strategy)
    ans = client.run(10, 10)
    assert ans == 20


def test_multiply():
    strategy: Strategy = StrategyMultiply()
    client = Client(strategy)
    ans = client.run(10, 10)
    assert ans == 100
