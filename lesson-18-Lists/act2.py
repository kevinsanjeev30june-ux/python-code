# List methods

list = [11,23,5,67,9]
print("Before sorting..")
print(list)
print("After sorting..")
print("Ascending order..")
list.sort()
print(list) 

print("Descending order..")
list.sort(reverse=True)
print(list)

# Reverse the list
list.reverse()
print("After reversing..")
print(list)

# append/add
list.append(500)
print(list)

# Remove() a specific item from the list
list.remove(67)
print(list)

# Remove the last item from the list
list.pop()
print(list)

# inset an new item at a specific position
list.insert(2, 23)
print(list)


# find sum
sum = 0
for item in list:
    sum += item 
print(f"Sum of the list is {sum}") 

# find the average
list_length = len(list)
average = sum / list_length
print(average)

# Find min and max
my_list2 = [11,2,78, 999, -5, 7,26]
my_list2.sort()

print(f"minimum : {my_list2[0]}")
print(f"maximum : {my_list2[-1]}")


# Slicing a list
print(my_list2[:3]) # first 3 items
print(my_list2[3:]) # all items except first 3
print(my_list2[2:4]) # items from index 2 to 4