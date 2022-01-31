from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_type(self):
        raise NotImplementedError()


class SUVEngine(Engine):
    def get_type(self):
        return "SUV"


class SportEngine(Engine):
    def get_type(self):
        return "Sport"
