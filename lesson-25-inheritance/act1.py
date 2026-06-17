# Inheritance in oop
class Grandpa:
    def __init__(self,name,money,car):
        self.name = name
        self.car = car
        self.money = money

    def displayAsset(self):
        return f"{self.name} has ${self.money} and also a {self.car} car"

class Grandson(Grandpa):
    pass
gp1 = Grandpa("Mr.JOHN ","25,00,000","Rolls Royce Phantom")
print(gp1.displayAsset())        