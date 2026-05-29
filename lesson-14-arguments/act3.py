# Recursion
   
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

number = int(input("Enter a number:"))
if number < 0:
    print("Invalid input...")
else:
    print(f"Factorial of {number} : {factorial(number)}")     