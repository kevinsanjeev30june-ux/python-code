# Initalize Dictionary
test_dict = {'Codingal': 2, 'is':2 ,'best': 2, 'for':2 , 'Coding' : 1}

# Printing the original dictionary
print("The original dictionary:" + str(test_dict))

# Initalize value 
K = 2

# using Loop
# Selective key values in dictionary

counter = 0
for key in test_dict:
    if test_dict[key] == K:
        counter = counter + 1

# Printing Result
print("Frequency of K is : " + str(counter))
