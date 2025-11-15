# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

username = input("Input your username: ")
password = input("Input your password: ")

if username == "pepe" and password == "asdasd":
    print("You enter to the system.")
else:
    print("Your username or password are incorrect.")