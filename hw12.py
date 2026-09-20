class Robot:
    def __init__(self, body, model):
         self.__body = body
         self.__model = model

    def __get_model(self):
        return f'Модель: {self.__model}'

    def get_secret_model(self):
        return self.__get_model()

    def __get_body(self):
        return f'Корпус: {self.__body}'

    def get_secret_body(self):
        return self.__get_body()

class Mecha(Robot):
    pass

robot = Mecha('алюминиевый', 'Heavy destroer')
print(robot.get_secret_body())
print(robot.get_secret_model())

    