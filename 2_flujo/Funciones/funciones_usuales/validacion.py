valor = input('dime algo bonito: ')
print (valor.isdigit() ) #solo digitos numeros.
print(valor.isalpha() ) #solo letras.
print(valor.isalnum() ) #numeros y letras.
print(valor.isnumeric() ) # si es numero.

## saber si una cadena de caracteres empieza , termina o incluye un determinado caracter.

texto = "en un lugar de la mancha"
print(texto.startswith('e')) # false
print(texto.endswith('a')) #true

#saber si algo esta incluido
busqueda = "lugar"
resultado = busqueda.lower() in texto.lower()
print('incluido' , resultado)