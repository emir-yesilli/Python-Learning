#---------------------------------------- Inheritance ----------------------------------------
class FamilyMembers():
    def __init__(self,name):
        self.name = name
        print("Family")

    def test1(self):
        print("test1")
    def test2(self):
        print("test2")

class MarriedFamilyMembers(FamilyMembers):
    def __init__(self,name):
        FamilyMembers.__init__(self,name)
        print("MarriedFamilyMembers")

    def test3(self):
        print("test3")

    #Override
    def test1(self):
        print("test1 override")

emir = FamilyMembers("Emir")
sila = MarriedFamilyMembers("Sila")

#------******-----
sila.test1()
sila.test2()
sila.test3()

# emir.test3() ----------> Error
