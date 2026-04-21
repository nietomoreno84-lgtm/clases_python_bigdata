texto ="David"

# un string es una cadena de caracteres, es decir es un conjunto de caracteres.

# cuantos caracteres tiene un texto.
print ( len(texto))  # cantidad de caracteres
print(texto[4]) # imprime la d
print(texto[0]) # imprime la D

texto = "David"

for i in range(len(texto)):
    print(texto[i])

# upper() lower()
# imprimir solo las mayusculas

for i in range(len(texto)):
    if texto[i] == texto[i].lower():
        print(texto[i])

