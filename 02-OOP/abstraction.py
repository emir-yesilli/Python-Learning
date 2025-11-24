#--------------------------------------- Abstraction ---------------------------------------
from abc import ABC, abstractmethod
class Car(ABC):

     @abstractmethod
     def maxSpeed(self):
         pass

class BMW(Car):
    def maxSpeed(self):
        print("Maximum speed is 200km/h")

bmw = BMW()
bmw.maxSpeed()