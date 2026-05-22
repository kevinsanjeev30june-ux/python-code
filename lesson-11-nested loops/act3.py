numbers = [1,3,4,3,6,8,9,2,3,4,6,2,3,9,3]
duplicates = []

# Find Duplicate numbers in the list:

for i in range(len(numbers)):
    for j in range(i + 1 ,len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers [i] not in duplicates:
                duplicates.append(numbers[i])
print("Duplicate number :", duplicates)                