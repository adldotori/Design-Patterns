from builder import Builder, CarBuilder, CarManualBuilder, Car, Manual
from engine import SUVEngine, SportEngine


class Director(object):
    def make_suv(self, builder: Builder):
        builder.reset()
        builder.setSeats(4)
        builder.setEngine(SUVEngine())
        builder.setTripComputer()
        builder.setGPS()

    def make_sports_car(self, builder: Builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer()
        builder.setGPS()


if __name__ == "__main__":
    director: Director = Director()
    builder: Builder = CarBuilder()
    director.make_sports_car(builder)
    car: Car = builder.getResult()

    builder: Builder = CarManualBuilder()
    director.make_sports_car(builder)
    manual: Manual = builder.getResult()

    print("Car >>>\n", car)
    print("Manual >>>\n", manual)
