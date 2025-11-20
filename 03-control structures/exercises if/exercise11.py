"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo
Si sólo dos lados del triángulo son iguales entonces es isósceles.
Si los 3 lados son iguales entonces es equilátero.
Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""

def clasificar_triangulo():
    print("--- CLASIFICADOR DE TRIÁNGULOS ---")
    # 1. Pedimos los datos (usamos float por si tienen decimales)
    a = float(input("Introduce el lado A: "))
    b = float(input("Introduce el lado B: "))
    c = float(input("Introduce el lado C: "))

    # 2. ORDENAMOS los lados. 
    # Esto es vital para Pitágoras. El lado más largo será 'lados[2]'
    lados = sorted([a, b, c])
    cateto1 = lados[0]
    cateto2 = lados[1]
    hipotenusa = lados[2]

    # Variables bandera (flags) para saber qué características tiene
    es_rectangulo = False
    tipo_lados = ""

    # 3. Comprobamos Pitágoras: c² = a² + b²
    # Usamos una pequeña tolerancia (0.001) por si hay decimales inexactos
    if abs(hipotenusa**2 - (cateto1**2 + cateto2**2)) < 0.01:
        es_rectangulo = True

    # 4. Clasificamos según la longitud de los lados
    if a == b and b == c:
        tipo_lados = "EQUILÁTERO"
    elif a == b or a == c or b == c:
        tipo_lados = "ISÓSCELES"
    else:
        tipo_lados = "ESCALENO"

    # 5. Mostramos el resultado final combinando las características
    print(f"\nEl triángulo es: {tipo_lados}")
    
    if es_rectangulo:
        print("Además, es un triángulo RECTÁNGULO (cumple Pitágoras).")

# Ejecutamos
clasificar_triangulo()