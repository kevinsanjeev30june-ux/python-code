# Reverse the string
word = input("Enter a word:")
rev_word = ''

for i in word :
    rev_word = i + rev_word

print("Originial string :",word)
print("reverse string :",rev_word)