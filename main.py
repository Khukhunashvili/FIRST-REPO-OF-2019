from colorama import Fore

x = 12
y = 1

print(Fore.GREEN)

for i in range(12):
    print(" "*x+"*"*y+"*"*y+" "*x)
    x-=1
    y+=1

for i in range(3):
    print(" "*11+"*"*4+" "*10)

print(Fore.RED)

print(" "*6+"Happy New Year ❤")
