# set of prime numbers
set_prime = {2,3,5,5,7,11,11}
print(set_prime)

# Copy set
# Shallow copy

set_prime_copy = set_prime.copy()
print(f"Original Set:{set_prime}")
print(f"copied Set:{set_prime_copy}")

# equality and identiity
print(set_prime == set_prime_copy )
print(set_prime is set_prime_copy)

# set from list
list = [1,2,2,3,4,4,5,6,6,7,7,6,7]
set1 = set(list)
print(set1)

# Set from tuple
t1 = (1,2,2,2,3,3,4,5,6)
set2 =  set(t1)
print(set2)

# set from dictionary
fruits ={
    1:" APPLE",
    2: "BANANA"
}
set3 = set(fruits.keys())
set4 = set(fruits.values())
print(set3)
print(set4)

# Adding members to a set(set_prime)
print("\n Adding elements to a set..") 
print('BEFORE ADDING...')
print(set_prime)

set_prime.add(13)
print("/n After adding") 
print(set_prime)


# Remove members from
set_prime.discard(13)
set_prime.discard(20)
print("\n After removing")
print(set_prime)

# 2.remove()
set_prime.remove(11)
try:
    print("Trying to remove")
    set_prime.remove(120)
    print("Removed successfully")
except KeyError:
    print("Element not present...")
finally:
    print("End program..")

print("After removal..")      
print(set_prime)

# 3 . pop()
popped_val = set_prime.pop()
print(f"\n Item removed :{popped_val}")
print(f" After removal :{set_prime}")

