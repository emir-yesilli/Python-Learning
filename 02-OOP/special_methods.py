class fruits():

    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name}: {self.calories} calories"

banana = fruits("banana",100)
print(banana)