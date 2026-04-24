
# =============================================================================
# EJERCICIO 3: PROCESADOR DE FRASES
# Pide al usuario una frase.
# Muestra:
#   - La frase con todas las palabras invertidas individualmente
#     (ej: "hola mundo" → "aloh odnum")
#   - devolver la cantidad de caracteres de la frase
#   - El número de veces que aparece cada vocal (a, e, i, o, u)
#   - La frase con los espacios reemplazados por guiones bajos
#   - La frase con palabras invertidad Tony Stark => Stark Tony
# =============================================================================
# devolver la cantidad de letras de la frase 
frase = input("Introduce una frase: ")

def cantidad_letras(frase):
    contador = 0
    for caracter in frase:
        if caracter.isalpha():
            contador +=1
    return contador

texto = input('dime algo bonito: ')
print(cantidad_letras(texto))

# numero de veces que aparace cada vocal

def contar_vocal(frase,vocal):
    return frase.count(vocal)

for vocal in "aeiouáéíóúÁÉÍÓÚAEIOU":
    numero = contar_vocal(texto, vocal)
    if numero != 0:
        print (vocal, numero)

def frase_con_separador(frase, separador):
    return frase.replace( " ", separador)

print(frase_con_separador(texto, '_'))


