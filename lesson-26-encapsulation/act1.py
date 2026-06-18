class Student:
    def __init__(self,name,age,pocketmoney):
        self.name = name

        # private variables
        # cant access directly
        self.__age = age
        self.__pocketmoney = pocketmoney

    # Getters and setters
    def getAge(self):
        return self.__age
    
    def setAge(self,age):
        self.__age = age

    def getPocketmoney(self):
        return self.__pocketmoney

    def setPocketmoney(self,pocketmoney):
        self.__pocketmoney = pocketmoney

if __name__ == "__main__":        

   s1 = Student("Kevin",13,2000)

   def displayAllDetails():
      print("Student Details...")
      print(s1.name)
      print(s1.getAge())
      print(s1.getPocketmoney())

   displayAllDetails()

while True:
    print("\nDo you want to update the info?")
    choice = input("Enter yes / no:")
    if choice not in ['yes' , 'y']:
        break
    newAge = int(input("\n Enter your new  age: "))
    newPocketMoney  = int(input("\n Enter your new pocketmoney: "))
    s1.setAge(newAge)
    s1.setPocketmoney(newPocketMoney)
    displayAllDetails()