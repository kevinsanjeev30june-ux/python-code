# Blueprint
class HotelBlueprint:

 # Initalizing object
 def __init__(self,name,rooms,floor,price):
  self.rooms =rooms
  self.floor = floor
  self.price = price
  self.name = name

  # custom method
 def displayDetails(self):
   print(f"This is{self.name} Hotel, It has {self.rooms} , {self.floor} floor, price per night is INR {self.price}/-")

# Create object from blueprint / class
# object is an instance of a class

ChennaiHotel = HotelBlueprint("Radison blu",100,10,'10000 \n')
HydrebadHotel = HotelBlueprint("\n Coromandel Hydrebad", 200,15,'20000\n')

ChennaiHotel.displayDetails()
HydrebadHotel.displayDetails()