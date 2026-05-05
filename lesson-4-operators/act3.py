# Take marks from the input
print("Enter marks obtained in 5 subjects:")
math = int(input("maths :"))
english = int(input("english:"))
science = int(input("science:"))
social = int(input("social:"))
tamil = int(input("tamil:"))

# calculate the percentage of marks
sum = math+english+science+social+tamil
print("Sum of math,english,science,social,tamil= ",sum)

percentage = (sum/500)*100
print("Percentage mark =",end="")
print(percentage)
