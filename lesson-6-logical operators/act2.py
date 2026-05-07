# Simple Mathematic Calculator
from colorama import Fore, init
init(autoreset = True)

print(f"{Fore.CYAN}Welcome to the python Calculator")
print("*"*30)

num1 = int(input("Enter your first number :"))
num2 = int(input("Enter second number :"))
print("Whicjh operation you want to perform ?1.ADD 2.SUBTRACT 3.MULTIPLY 4.DIVISION")
print("Enter 1/2/3(/4")
result = 0
choice = int(input("Enter your choice :"))

if choice == 1:
    result = num1 + num2
    print(f"The result of addition of {num1} and {num2} :{Fore.CYAN}{result}")
elif choice == 2:
    result = num1 - num2
    print(f"The result of subtraction of {num1} and {num2} :{Fore.CYAN}{result}")
elif choice == 3:
    result = num1 * num2
    print(f"The result of multiplication of {num1} and {num2} :{Fore.CYAN}{result}")
elif choice == 4:
    result = num1 / num2
    print(f"The result of division of {num1} and {num2} :{Fore.CYAN}{result}")

else:
    print(f"{Fore.RED}Invalid input")                