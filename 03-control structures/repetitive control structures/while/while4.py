secret = "asdasd"

while True:
    password = input("Input your password: ")
    if password != secret:
        print("Incorrect password")
    if password == secret:
        break

print("Welcome")
print("Finishing program")