class Animal:
    def make_sound(self):
        print("Some generic sound")

    def move(self):
        print("Some generic movement")


class Dog(Animal):
    def make_sound(self):
        print("Bark!")

    def move(self):
        print("Run")


def cause_action(animal_object):
    animal_object.make_sound()
    animal_object.move()


my_dog = Dog()
cause_action(my_dog)
