class Car:
    def __init__(self, color, brend, vin, owner):

        self.color = color
        self.brend = brend
        self.__vin = vin
        self.__owner = owner

    def drift(self, drift):
            return f"{self.color} {self.brend} очень круто {drift}!"


    def make_sound(self,sound):
         return f"{self.color} ({self.brend}) она делает {sound} "

    def get_vin(self):
         return f'VIN number : {self.__vin}'

    def __get_owner(self):
         return f'у неё есть {self.__owner}'

    def get_secret_owner(self):
         return self.__get_owner()

class Racing(Car):
   
    def make_sound(self):
         return "Врум-Врум!"


racing = Racing("красная","Ламбарджини", "30440140130513", "владелец-Дима")
print(racing.drift("дрифтит"))
print(racing.make_sound())
print(racing.get_vin())
print(racing.get_secret_owner())