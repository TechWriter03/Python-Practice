# Method Overloading
class Calculator:

    def add(self,a=0,b=0,c=0):
        print(a+b+c)
    
    def sub(self,a=0,b=0):
        print(a-b)
    
calc=Calculator()
calc.add(1)
calc.add(1,2)
calc.add(1,2,3)
calc.sub(5)
calc.sub(5-2)

# Method Overriding
class Car:

    def start(self):
        print("Starting the car")

class BMW(Car):

    def start(self):
        print("Starting the BMW")

car1=BMW()
car1.start()
