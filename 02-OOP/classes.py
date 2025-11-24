#---------------------------------------- Classes ----------------------------------------
class Person():
    #property
    '''
    name = ""
    surname = ""
    age = int()

    '''
    gender = ""
    # initialize method
    def __init__(self, nameInput, surnameInput, ageInput):
        self.name = nameInput
        self.surname = surnameInput
        self.age = ageInput

    def printName(self):
        print(self.name)

emir = Person("Emir","Yesilli",18)

emir.gender = "Male"
print(emir.age)
emir.printName()
print(emir.gender)

