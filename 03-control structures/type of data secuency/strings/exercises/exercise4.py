# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

cont = 0
pos = 0
cad = input("Introduce una cadena: ")
# Elimino los posibles espacios que haya al principio y al final de la cadena
cad = cad.strip()
# Voy buscando los espacios
pos = cad.find(" ", pos)
while pos != -1:
    cont = cont + 1
    # No tengo en cuenta los posibles espacios que haya entre las palabras
    while cad[pos+1] == " ":
        pos = pos+1
    pos = cad.find(" ", pos + 1)
print("La frase tiene",cont+1," palabras.")