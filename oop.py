from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def test(self):
        pass

class TestCar(Car):
    def car(self):
        print("car")

    def test(self):
        print('test')

car = TestCar()
print(car.car())