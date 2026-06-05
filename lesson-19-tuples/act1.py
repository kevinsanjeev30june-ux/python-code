# Create a Tuple

myTuple_1 = ("Tuple" , False, 3.255,100)
print(myTuple_1)

# Create another Tuple
myTuple_2 = (4,9,2,11,90,23,7)
print(myTuple_2)

# Tuple is immutable , so we cannot add new element to existing Tuple
myTuple_2 = myTuple_2 + (100,)
print(myTuple_2)

# Count total number of items in Tuple
t1 = (50,10,75,80,45,12)
print(t1.count(50))

# Slice a Tuple
print(t1[1: 3])
print(t1[3:])
print(t1[-1])