secret = "asdasd"
password = input("Input your password: ")
while password != secret:
    print("Incorrect password")
    other = input("Do you want to input other password (Y/N)?: ")
    if other.upper()=="N":
        break
    password = input("Input your password: ")
if password == secret:
    print("Welcome")
print("Finishing program...")