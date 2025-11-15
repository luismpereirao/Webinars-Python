#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
cadena = input("Introduce una cadena de texto: ")
dict = {}
for caracter in cadena:
    if caracter in dict:
        dict[caracter]+=1
    else:
        dict[caracter]=1
    
for key, value in dict.items():
    print(key,"->",value)