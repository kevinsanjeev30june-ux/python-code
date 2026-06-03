# Function Calculator

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

print(" Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter choice (1/2/3/4): "))
    num1 = float(input("Enter first number: ")) 
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 3:
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 4:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice.")

except ValueError:
    print("Error: Please enter a number.")
finally:
    print("Thank you for using the calculator.")   