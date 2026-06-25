from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):
    @abstractmethod
    # This method has to be implemented in its subclass and compulsory
    def move(self):
        pass

    # normal method not abstract
    def test(self):
        pass

class Snake(Animal):
    @override
    def move(self):
        print("Snakes crawl")

class Horse(Animal):
    @override
    def move(self):
        print("Horse Kicks")

class Birds(Animal):
    @override
    def move(self):
        print("Birds fly")

# S = Snake()                          
# S.move()

# H = Horse()
# H.move()

# B = Birds()
# B.move()

# ---Object Creation in first loop
# 1. Put the classes themselves into a list
animal_classes = [Snake, Horse , Birds]

# 2. LOOP through the classes, instantiate them, and call move()
for animal_class in animal_classes:
    animal_object = animal_class() 
    # Create the object (e.g, Snake(),Horse(),Birds() )
    animal_object.move()