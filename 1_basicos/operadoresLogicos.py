# and , or , not

precio = float (input('dime un precio:'))
marca = input ('dime una marca: ')

resultado = precio > 100 and marca == "nike"
print(resultado)

# numero par o divisible por 5
# 1. pedir el numero
# 2. hacer la comparacion

numero = float(input('introduce un numero: '))
# es_par = numero % 2 == 0
# multiplo_5 = numero % 5 == 0



resultado = numero % 2 == 0 or numero % 5 == 0
print(resultado)

# operador de negacion

esta_activo = True
print (not esta_activo)

