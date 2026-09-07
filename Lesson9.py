class Animal:
    def __init__(self, name, species):
        
        self.name = name          
        self.species = species    

    
    def make_sound(self, sound):
        return f"{self.name} ({self.species}) говорит: {sound}!"

   
    def eat(self, food):
        return f"{self.name} с аппетитом ест {food}."

   
    def sleep(self):
        return f"{self.name} свернулся клубком и уснул. Хр-р-р..."


class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return 'Мяу-Мяу-Мяу'
    
cat = Cat("Перси")
print(cat.eat("корм"))
print(cat.make_sound())       

