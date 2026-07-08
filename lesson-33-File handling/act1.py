file = open('kevin.txt', 'r')
content = file.readlines()

for line in content:
    print(line)

with open('kevin.txt', 'r') as file2:
    new_content = file2.readlines()
    for line in new_content:
        print(line)
