words = []
while True:
    word = input("Enter a word(type'stop to end'):")

    if word.upper() == 'STOP':
        break
    words.append(word)
print("\nWords entered...")

for w in words:
    print(w)