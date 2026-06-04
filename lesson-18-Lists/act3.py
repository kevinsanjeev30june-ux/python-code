# Check palindrome
word = input("Enter a word: ")
reversed_list = []
 
# Convert the word to lower case
word = word.lower()
 
# Convert the word to list
word_list = list(word)
print(word_list)

# Reversed
for ch in reversed(word_list):
    reversed_list.append(ch)

if word_list == reversed_list:
    print(" This is a palindrome.")
else:
    print(" This is not a palindrome.")    