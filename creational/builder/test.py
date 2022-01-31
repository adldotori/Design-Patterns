from main import Director
from builder import Builder, CarBuilder, CarManualBuilder, Car, Manual


class Test(object):
    def test_sports_car(self):
        director: Director = Director()
        builder: Builder = CarBuilder()
        director.makeSportsCar(builder)
        car: Car = builder.getResult()

        builder: Builder = CarManualBuilder()
        director.makeSportsCar(builder)
        manual: Manual = builder.getResult()

        print("Car >>>\n", car)
        print("Manual >>>\n", manual)

    def test_suv(self):
        director: Director = Director()
        builder: Builder = CarBuilder()
        director.makeSUV(builder)
        car: Car = builder.getResult()

        builder: Builder = CarManualBuilder()
        director.makeSUV(builder)
        manual: Manual = builder.getResult()

        print("Car >>>\n", car)
        print("Manual >>>\n", manual)
