# metodos de union
nombre = "David"
apellido = "Nieto"
edad = 41
separador = " - "

texto = F"{nombre}{separador}{apellido}{separador}{edad}"


otro_texto = separador.join([nombre, apellido, str(edad)])
print(texto)
print(otro_texto)