# Single Inheritance
class Car:

    def __init__(self,brand):
        self.brand=brand

    def printBrand(self):
        print("Brand:",self.brand)

class Tata(Car):

    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

    def printModel(self):
        print("Model:",self.model)

    def getDetails(self):
        super().printBrand()
        self.printModel()

car=Tata("TATA","NEXON")
car.getDetails()

# Multiple Inheritance
class Father:

    def skills(self):
        print("Knows Driving")

class Mother:

    def skills(self):
        print("Knows Cooking")

class Child(Father,Mother):

    def __init__(self):
        self.skills()
        Mother.skills(self)
        print("Knows Coding")

child=Child()
