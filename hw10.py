class Car:
    def __init__(self, color, brend):

        self.color = color
        self.brend = brend

    def drift(self, drift):
            return f"{self.color} {self.brend} очень круто {drift}!"


    def make_sound(self,sound):
         return f"{self.color} ({self.brend}) она делает {sound} "

class Racing(Car):
   
    def make_sound(self):
         return "Врум-Врум!"

racing = Racing("красная","Ламбарджини")
print(racing.drift("дрифтит"))
print(racing.make_sound())