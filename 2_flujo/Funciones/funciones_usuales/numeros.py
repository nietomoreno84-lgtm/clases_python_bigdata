# python tiene una libreria especial para funciones matemáticas complejas math. Para usarla tenemos que importarla al principio del script
# tiene libreria operaciones matematicas math
# https://docs.python.org/3/library/math.html

import math

# funciones de conversion
numero = 5
print( float(numero) ) # 5.0 racional
print( int(3.3) ) # 3 integer

# a modo reto 
nota = 4.999999999999999999
print(nota)

# redondeo de un numero
numero = 4.567892
print( round(numero, 4) ) # matematico

# redondeo a la alta
print(math.ceil(numero)) #5
# redondeo a la baja
print(math.floor(numero)) #4
