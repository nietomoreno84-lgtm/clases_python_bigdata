# realizar una funcion que me permita evaluar si un numero introducido por parametro es o impar

def evaluar_paridad():
    numero = int(input("Introduce un número: "))

    if numero == 0:
        print("Es cero")
    elif numero % 2 == 0:
        print("Es par")
    elif numero % 2 != 0:
        print ('es impar')    
    else:
        print("El valor no es un numero")


evaluar_paridad()

# Realizar una funcion que me introduzca un texto y me cuente sus vocales.

def contar_vocales():
    texto = input("Introduce un texto: ")
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vocales:
            contador += 1

    print("Número de vocales:", contador)


contar_vocales()

# Realizar una funcion que introduzca el nombre de una persona y me devuelve solo sus iniciales

def obtener_iniciales():
    nombre = input("Introduce el nombre completo: ")
    
    palabras = nombre.split()
    iniciales = ""

    for palabra in palabras:
        iniciales += palabra[0].upper()

    print("Iniciales:", iniciales)

# Ejecutar
obtener_iniciales()