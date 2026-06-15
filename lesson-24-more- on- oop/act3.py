def find_duplicates(items):
    appearance_tracker={}
    duplicates ={}

    for i ,item in enumerate(items):
        if item in appearance_tracker:
            appearance_tracker[item].append(i)
            duplicates[item] = appearance_tracker[item]

        else:
            appearance_tracker[item] = [i] 

    return duplicates 
   
names_list =  ["A","B","C","A","B"]
duplicate_results = find_duplicates(names_list)  

if duplicate_results:
    for name ,indices in duplicate_results.items():
        print(f"'{name}' is duplicated at indices: {indices}")

else:
    print("No  duplicates found!!!")        