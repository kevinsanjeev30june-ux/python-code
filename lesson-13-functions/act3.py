# Simple Calculator

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def div(x,y):
    return x * y
def mul(x,y):
    return x // y

print("Welcome to Calculator.....")
print("*"*30)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter Second number : "))

print("Enter your choice 1/2/3/4")
print("1.  ADD")
print("2.  SUBTRACT")
print("3.  MULTIPLY")
print("4.  DIVISION")

choice = int(input("Enter choice : "))

if choice == 1:
    print(f"The result of addition of {num1} and {num2} is {add(num1,num2)}")

elif choice == 2:
    print(f"The result of subtraction of {num1} and {num2} is {sub(num1,num2)}")

elif choice == 3:
    print(f"The result of multiplication of {num1} and {num2} is {mul(num1,num2)}")

elif choice == 4:
    print(f"The result of division of {num1} and {num2} is {div(num1,num2)}")

else:
    print("Invalid...input...")


