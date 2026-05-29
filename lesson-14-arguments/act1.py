def total_bill(bill_amount,tip = 100.5):
    total = bill_amount *(1*0.01* tip)
    total = round(total,2)
    return total

bill_amount = float(input("Enter the bill amount:"))    
tip_amount = float(input("Enter the tip amount:"))

total_bill_amount = total_bill(bill_amount , tip_amount)
print(f"Total bill: {total_bill_amount}")