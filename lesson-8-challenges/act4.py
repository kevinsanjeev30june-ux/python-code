a = int(input("Enter a value :"))
b = int(input("Enter a value 2 :"))
c = int(input("Enter a value 3 :"))

avg = (a+b+c) / 3
avg = round(avg,2)
print(f"avg = {avg :.2f}")

if avg > a and avg > b and avg > c:
    print("%.2f is higher than %d,%d,%d"%(avg,a,b,c))
elif avg > a and avg > b : 
    print("%.2f is higher than %d,%d,"%(avg,a,b))
elif avg > a and avg > c : 
    print("%.2f is higher than %d,%d,"%(avg,a,c))    
else:
    print("Invalid input")
       