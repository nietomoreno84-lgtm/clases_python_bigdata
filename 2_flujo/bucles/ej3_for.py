#quiero pedir un texto por pantalla d cualquier longitud y quiero que pidais una vocal

# contar cuantas vocales tiene el texto

# paso 1 pidse un texto
texto = input ('Dame una frase maravillosa:').lower()
# paso 2 pedir una vocal
vocal = input ('Dame un vocal:').lower()

cantidad= len(texto)
# paso 3: pintar todos los caracteres del texto
#paso 4 imprimir solo la vocal pedida
#contar las vocales . crear una variable que incremente en 1 cada vez que encuentre mi vocal
numero_vocales = 0
for i in range(cantidad):
    if texto[i] == vocal:
       numero_vocales = numero_vocales + 1
