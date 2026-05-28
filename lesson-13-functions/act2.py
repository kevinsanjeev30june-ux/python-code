count = 0
def increment():
    global count
    count += 1

for i in range(1,7):
    increment()

print(count)