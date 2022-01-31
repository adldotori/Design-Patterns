from abc import ABC, abstractmethod
from engine import Engine


class Car(object):
    seats = 0
    engine = None
    trip_computer = False
    gps = False

    def __str__(self):
        ret = ""
        ret += f"Car with {self.seats} seats, {self.engine.get_type()} engine\n"
        if self.trip_computer:
            ret += "with trip computer\n"
        if self.gps:
            ret += "with GPS\n"
        return ret


class Manual(object):
    seats = 0
    engine = None
    trip_computer = False
    gps = False

    def __str__(self):
        ret = ""
        ret += f"Car with {self.seats} seats, {self.engine.get_type()} engine\n"
        if self.trip_computer:
            ret += "with trip computer\n"
        if self.gps:
            ret += "with GPS\n"

        return ret


class Builder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def setSeats(self, seats: int):
        raise NotImplementedError()

    @abstractmethod
    def setEngine(self, engine: Engine):
        raise NotImplementedError()

    @abstractmethod
    def setTripComputer(self):
        raise NotImplementedError()

    @abstractmethod
    def setGPS(self):
        raise NotImplementedError()


class CarBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__car = Car()

    def setSeats(self, seats: int):
        self.__car.seats = seats

    def setEngine(self, engine: Engine):
        self.__car.engine = engine

    def setTripComputer(self):
        self.__car.trip_computer = True

    def setGPS(self):
        self.__car.gps = True

    def getResult(self):
        return self.__car


class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.__manual = Manual()

    def setSeats(self, seats: int):
        self.__manual.seats = seats

    def setEngine(self, engine: Engine):
        self.__manual.engine = engine

    def setTripComputer(self):
        self.__manual.trip_computer = True

    def setGPS(self):
        self.__manual.gps = True

    def getResult(self):
        return self.__manual
