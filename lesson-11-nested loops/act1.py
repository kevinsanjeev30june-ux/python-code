# Matrix of n/n
upper_outer = int(input("Enter the upper limit of the outer matrix:"))
upper_inner = int(input("Enter the upper limit of the inner matrix:"))

for i in range(1,upper_outer + 1):
    for j in range(1,upper_outer + 1):
        print("*", end = '')

    print()   
    