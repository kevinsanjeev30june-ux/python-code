from colorama import Fore , init
init(autoreset = True)

number = int(input("Enter your number:"))

for i in range(1,11):
    if number == i :
        break
    print(f"{Fore.CYAN}{i}")
print("*"*30)

for i in range(1,11):
    if number == i :
        continue
    print(f"{Fore.GREEN}{i}")


print("*"*30)

for i in range(1,11):
    if number == i :
        pass
    print(f"{Fore.LIGHTYELLOW_EX}{i}")