# Using try and except

try:
    number = int(input("Enter a number: "))
    print("The number you entered is:", number)
#Using value error
except ValueError as ex:
    print("Exception:",ex)
    