account_balance = 5000

try:
    amount = float(input("Enter the amount to withdraw: "))
    
    if amount > account_balance:
        raise ValueError("Insufficient balance in your account.")

    account_balance -= amount
    print(f"Withdrawal successful. Remaining balance: {account_balance}")

except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Thank you for banking with us.")    