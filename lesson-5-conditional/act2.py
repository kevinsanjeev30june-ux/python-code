originial_cost = float(input("Enter the actual price of item :"))
sale_amount = float(input("Enter the sale amount :"))


if(sale_amount > originial_cost):
    profit_amount = sale_amount - originial_cost
    print(f"Total profit :{profit_amount}")

else:
    print("No profit!!")