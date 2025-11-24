#--------------------------------------- Exercises ---------------------------------------
#Bank Simulator
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print(self.balance)

akbank = BankAccount("AkBank", 100)
akbank.deposit(50)
akbank.withdraw(20)