# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def EsMultiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

if EsMultiplo(num1,num2):
    print(num1, "es múltiplo de ", num2)
else:
    print(num1, "no es múltiplo de ", num2)