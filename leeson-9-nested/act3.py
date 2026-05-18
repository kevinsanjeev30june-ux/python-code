print("select your ride:")
print("1.Bike")
print("2.Car")

# take input of number 1 or 2 
# Select your ride
choice = int(input("Enter your choice :"))

# user entering option 1
if ( choice == 1): #condition 1 if outer statement
    print("What type of bike?")
    print("1.scooty\n")
    print("2.scooter\n")

  # condition for selecting the type of bike 
    choice2 = int(input("Enter your choice2:"))
    if choice2 == 1: # inner elif statement
      print("You have selected scooty")
    else:    
      print("You have selected scooty")

 # user entering option 2 
elif( choice == 2): # outer elif staement
   print("What type of car")
   print("1. Sedan")
   print("2. Xuv")  
   choice3 = int(input("Enter your choice :"))
   
   if choice3 == 1:# inner if statement
   #condition for selecting the type of car
        print("You have selected sedan")
   else:     
        print("You have selected Xuv")
   
else: # outer else statement
    print("Wrong choice !")    