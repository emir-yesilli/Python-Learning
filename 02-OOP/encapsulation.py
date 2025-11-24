#--------------------------------------- Encapsulation --------------------------------------
class Phone():
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def info(self):
        print(f"{self.name} price is {self.__price}")
    def changePrice(self,price):
        self.__price=price

iphone = Phone("iPhone",1000)
iphone.info()

iphone.price = 800
iphone.info()

iphone.changePrice(500)
iphone.info()