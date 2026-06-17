# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def ff(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def ff(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object creation 
peggy = Penguin()
peggy.ff()
peggy.swim()
peggy.run()