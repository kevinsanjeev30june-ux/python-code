# Taking User input amd printing them
class IOString:
    def __init__(self):
        self.name = ""

    # Getter method to accept
    def getName(self):
        self.name = input("Enter the name:").strip().upper()

    # printing Name in Capital letter
    def displayName(self):
        print(f"Your name is {self.name}")

# Create an Object of IOString class
il = IOString()
il.getName() # Ask for input
il.displayName() # Display           