# Check if it is divisible

numerator = int(input("Enter the numerator :"))
denominator = int(input("Enter the denominator :"))

if numerator % denominator == 0:
    print(f"{str(numerator)} is divisible by {str(denominator)}")

else:
    print(f"{str(numerator)} is not divisible by {str(denominator)}")
        