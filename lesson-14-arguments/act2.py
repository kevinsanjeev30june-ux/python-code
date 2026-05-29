def cube(n):
    return n**3

def cube_of_odd(n):
    if n% 2 != 0:
        return cube(n)
    else:
        return None
    
number = int(input("Enter a number:"))
print(cube_of_odd(number))    