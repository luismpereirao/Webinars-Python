cont = 0
for var in range(1,6):
    num = int(input("Input a number: "))
    if num % 2==0:
        cont = cont+1
print("You entered ", cont, " pair numbers.")