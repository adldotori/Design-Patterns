from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass


class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"{self.x}, {self.y}: ."

    def move(self, x, y):
        self.x = x
        self.y = y


class Circle(Dot):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def draw(self):
        return f"{self.x}, {self.y}: o"


class CompoundGraphic(Graphic):
    def __init__(self, *graphics: List[Graphic]):
        self.children = list(graphics)

    def add(self, graphic: Graphic):
        self.children.append(graphic)

    def remove(self, graphic: Graphic):
        self.children.remove(graphic)

    def draw(self):
        return "\n".join([graphic.draw() for graphic in self.children])

    def move(self, x, y):
        for graphic in self.children:
            graphic.move(x, y)
