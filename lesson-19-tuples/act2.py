# Palindrome using tuple

def palindromeChecker(tuple):
    end = len(tuple) - 1
    start = 0

    while start < end:
        if(tuple[start] != tuple[end]):
            return False
        start += 1
        end -= 1
    return True 


word = input("Enter a word: ").upper()
tuple = tuple(word)

if palindromeChecker(tuple):
    print("The given tuple is a palindrome")
else:
    print("The given tuple is not a palindrome")