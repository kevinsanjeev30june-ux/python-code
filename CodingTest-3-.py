# Dictionary with student names and scores
grades = {
    "Alice": 85,
    "Kevin": 92,
    "Charlie": 78,
    "David": 88,
    "Sara": 95
}

# average    
average = sum(grades.values()) / len(grades)
print("Average:", average)

# Top and bottom scorer
top = max(grades, key=grades.get)
bottom = min(grades, key=grades.get)

print("Top Scorer:", top, grades[top])
print("Bottom Scorer:", bottom, grades[bottom])

# Search student
name = input("Enter student name: ")
print(name, "score:", grades.get(name, "Not found"))