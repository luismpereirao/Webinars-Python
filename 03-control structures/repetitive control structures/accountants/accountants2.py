sum = 0
for var in range(1,6):
    num = int(input("Input a number"))
    if num % 2 == 0:
        sum = sum + num

print("Sum of pair numbers is ", sum)