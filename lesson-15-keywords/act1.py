while True:
 word = input("Enter a word:")
 if word == 'stop':
        break
 search_key = input("Enter the search key:")

 if len(search_key) > 1:
    print("Reenter one word only")
    continue 
 for letter in word:
     if letter == search_key:
         print("Letter found")
         break
 else:
     print("Letter not found") 