# Destructor

class Employee:
    def __init__(self):
        self.name = ""

    def getName(self):
        self.name = input("Enter name:")

    
    def displayName(self):
        print(f"Name :{self.name}")

    def __del__(self):
        print("Object is destroyed automatically")

# create object
def CreateObject():
    print("Object creation started...") 
    el = Employee()
    print("Object successsfully created")  
    return el
             
print("Start..")
obj1 = CreateObject()
print("Program ends...")
