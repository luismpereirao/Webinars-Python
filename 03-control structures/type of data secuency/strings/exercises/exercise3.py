# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cad = input("Introduce una cadena de texto: ")

while True:
    car = input("Introduce un caracter: ")
    if len(car) > 1:
        print("Me tienes que dar un solo caracter")
    if len(car) == 1: break

print(f"En la cadena {cad} aparecen {cad.count(car)} veces el caracter {car}")