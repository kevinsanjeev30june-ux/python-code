# Inheritance in oop
class Grandpa:
    def __init__(self,name,money,car):
        self.name = name
        self.car = car
        self.money = money

    def displayAsset(self):
        return f"{self.name} has ${self.money} and also a {self.car} car"

class Grandson(Grandpa):
    def __init__(self,name,money,car,laptop):
        super().__init__(name,money,car)
        self.laptop = laptop

    def displayAsset(self):
          return f"{super().displayAsset()}, and {self.laptop} laptop"
    
gs1 = Grandson("Kevin","25,00,000" ,"Rolls Royce Phantom", "lenovo slim 3")
print(gs1.displayAsset())    