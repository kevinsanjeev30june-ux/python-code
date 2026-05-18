units_consumed = float(input("Enter the number of units you have consumed this month:"))

bracket_1 = 50*2.6
bracket_2 = 50*3.25
bracket_3 = 100*5.26

if units_consumed < 50 :
    amount = units_consumed *2.60
    tax = 25

elif units_consumed <= 100:
    amount = bracket_1 + ((units_consumed - 50) * 3.25)
    tax = 35

elif units_consumed <= 200:
    amount = bracket_1 + bracket_2 ((units_consumed - 100) * 5.26)
    tax = 45

elif units_consumed >100:
    amount = bracket_1 + bracket_2 + bracket_3 ((units_consumed - 200) * 8.45)
    tax = 75     

else:
    print("Enter a valid input")

total_amount = amount + tax
print("\n Electricity Bill: ", total_amount)      