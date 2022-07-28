# Constructor and Destructor
class Person:
    def __init__(self, name, age):
        print("Person Created")
        self.name = name
        self.age = age
    def printInfo(self):
        print(self.name, self.age)
    def __del__(self):
        print(self.name, "Object Destroyed")

P1 = Person("Mats", 19)
P2 = Person("Asim", 27)
P1.printInfo()
P2.printInfo()
del P2
input()
