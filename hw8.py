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

    
my_pet = Animal("Перси", "Кошка")


print(my_pet.name)     
print(my_pet.species)  


print(my_pet.make_sound("Мяу"))  
print(my_pet.eat("корм, мясо, рыбу"))        
print(my_pet.sleep())          

