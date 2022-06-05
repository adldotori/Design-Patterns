from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, x: int, y: int):
        pass


class StrategyAdd(Strategy):
    def execute(self, x: int, y: int):
        return x + y


class StrategyMultiply(Strategy):
    def execute(self, x: int, y: int):
        return x * y
