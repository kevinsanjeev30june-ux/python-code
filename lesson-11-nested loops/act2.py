# write a program to print all prime numbers 
lower_range = int(input("Enter a lower range:"))
upper_range = int(input("Enter a upper range:"))

for num in range(lower_range , upper_range + 1):
    if num > 1 :
        for i in range (2,num):
            if (num % i) == 0:
                break

        else:
            print(num)    