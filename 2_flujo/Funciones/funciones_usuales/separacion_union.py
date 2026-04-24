# metodos de union
nombre = "David"
apellido = "Nieto"
edad = 41
separador = " - "

texto = F"{nombre}{separador}{apellido}{separador}{edad}"


otro_texto = separador.join([nombre, apellido, str(edad)])
print(texto)
print(otro_texto)

# metodos de separacion

frase = "El presidente dijo: Hola como estan los maquinas"
resultado = frase.partition(": ")
print(resultado[2])

# split()

texto = "Porque la vida puede ser maravillosa"

resultado = texto.split(' ')
#crear un conjunto de elemnteos sin el espacio en blanco
print(resultado[5])

#splitlines() me permite separar lineas en un texto multilinea

cadena = """ Hola
bienvenido
al
maravilloso
mundo
python
"""

print(cadena)

conjunto_lineas = cadena.splitlines()
print(conjunto_lineas)

# deletrear una cadena de texto cualquiera

palabra = "supercalifragilistico"
print(list(palabra))
