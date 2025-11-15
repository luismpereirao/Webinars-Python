indicator = False
for var in range(1,6):
    num = int(input("Input a number: "))
    if num % 2 == 0:
        indicator = True
if indicator:
    print("You entered some pair numbers")
else:
    print("You not entered none pair numbers")