import math


class RoundHole(object):
    def __init__(self, radius: float):
        self.radius = radius

    def fits(self, peg: object) -> bool:
        return self.radius >= peg.get_radius()


class RoundPeg(object):
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius


class SquarePeg(object):
    def __init__(self, width: float):
        self.width = width

    def get_width(self) -> float:
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg: SquarePeg):
        self.square_peg = square_peg

    def get_radius(self) -> float:
        return self.square_peg.get_width() * math.sqrt(2) / 2
