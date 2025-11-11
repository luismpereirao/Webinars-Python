# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

name = input("Introduce tu nombre: ")
lastname = input("Introduce tus apellidos: ")

inicial_nombre = name[0]
inicial_apellidos= lastname[0]

print(f"Las iniciales del nombre {name} {lastname} son {inicial_nombre.upper()} y {inicial_apellidos.upper()}")