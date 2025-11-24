#--------------------------------------- Polymorphism ---------------------------------------
class Dog():
    def __init__(self,name):
        self.name=name
    def info(self):
        return self.name + " is a dog."

class Cat():
    def __init__(self,name):
        self.name=name

    def info(self):
        return self.name + " is a cat."

barley = Dog("Barley")
garfield = Cat("Garfield")
animalList = [barley,garfield]
for x in animalList:
    print(x.info())
