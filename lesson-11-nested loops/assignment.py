matrix = [[1,2,3],[5,6,7], [8,9,10]]

print("Even elements in the matrix:")

for row in matrix:
    for element in row:
        if element % 2 == 0:
            print(element)