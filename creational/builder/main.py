from builder import Builder, CarBuilder, CarManualBuilder, Car, Manual
from engine import SUVEngine, SportEngine


class Director(object):
    def makeSUV(self, builder: Builder):
        builder.reset()
        builder.setSeats(4)
        builder.setEngine(SUVEngine())
        builder.setTripComputer()
        builder.setGPS()

    def makeSportsCar(self, builder: Builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer()
        builder.setGPS()


if __name__ == "__main__":
    director: Director = Director()
    builder: Builder = CarBuilder()
    director.makeSportsCar(builder)
    car: Car = builder.getResult()

    builder: Builder = CarManualBuilder()
    director.makeSportsCar(builder)
    manual: Manual = builder.getResult()

    print("Car >>>\n", car)
    print("Manual >>>\n", manual)
