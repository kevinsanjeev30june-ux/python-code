# Create a list of fruits
fruits = ["apple", "banana", "kiwi", "kiwi", "banana", "pineapple"]

fruit_count = {}
# Counnt the occurences of each fruit
for fruit in fruits:
    fruit_count[fruit] =fruits.count(fruit)
    

# print the counts of each fruit
print(fruit_count)
