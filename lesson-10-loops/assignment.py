# program to enter words by user

words = []

for i in range(100): # large limit for asking
    
    word = input("Enter a word: ")

    if word == "stop":
        break

    words.append(word)

print("Words entered:")
for w in words:
    print(w)