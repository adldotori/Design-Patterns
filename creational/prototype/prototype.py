from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        raise NotImplementedError()


class ConcretePrototype(Prototype):
    def __init__(self, name: str):
        self.name = name

    def clone(self):
        return ConcretePrototype(self.name)

    def __str__(self) -> str:
        return "name: {}".format(self.name)

    def __eq__(self, o) -> bool:
        return self.name == o.name


class SubClassPrototype(ConcretePrototype):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def clone(self):
        return SubClassPrototype(self.name, self.age)

    def __str__(self) -> str:
        return "name: {}, age: {}".format(self.name, self.age)

    def __eq__(self, o) -> bool:
        return self.name == o.name and self.age == o.age
