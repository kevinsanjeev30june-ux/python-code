num = int(input("Enter a number:"))
original = num
digits = []

while num > 0:
    digit = num % 10
    digits .append(digit)
    num = num // 10

total = 0
for digit in digits:
    total += digit ** len(digits)

print("Calculated value :",total)

if total == original:
    print("Armstrong number")

else:
    print("Not an armstrong number")    