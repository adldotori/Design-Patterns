from strategy import Strategy, StrategyAdd, StrategyMultiply


class Client(object):
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def run(self, x, y):
        return self.strategy.execute(x, y)


if __name__ == "__main__":
    strategy: Strategy = StrategyAdd()
    client = Client(strategy)
    ans = client.run(10, 10)
    print(ans)
