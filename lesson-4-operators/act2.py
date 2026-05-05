Amount = int(input("Enter the amount to withdraw :"))

note_100 = Amount//100
note_50 = (Amount % 100)//50
note_10 =((Amount % 100)%50)//10

print("Notes of 100 :",note_100)
print("Notes of 50 :",note_50)
print("Notes of 10 :",note_10)
