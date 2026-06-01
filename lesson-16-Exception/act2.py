# Using multiple except blocks for different type of errors
try:
    num1,num2 = eval(input("Enter two numbers separated by comma: "))
    result = num1/num2
    print("The result  is:", result)

except ZeroDivisionError :
    print("You cannot divide a number by zero")

except SyntaxError:
    print("Please enter two numbers separated by comma")

except:
    print("Wrong input")    
else:
    print("no exception occurred")

finally:    
    print("This will always execute")