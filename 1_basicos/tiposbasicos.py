nombre_alumno ="David Nieto"
print (nombre_alumno) # David Nieto
print(type(nombre_alumno))

nombre_alumno = 21
print (nombre_alumno)
print(type(nombre_alumno))

# tipos basicos en Python

# Numericos

edad = 36
grados = -27
precio = 1299.35

# booleano

estado = True
activo = False

# cadena de caracteres - string

nombre = "Laura"
apellidos ='Martinez'
mensaje = 'El niño dijo: "que pasa"'
print (mensaje)

# Laura Martinez : 36
nombre_completo = nombre + " " + apellidos + ":  " + str(edad)
print(nombre_completo)

nombre_completo2 = f'{nombre} {apellidos}: {edad}'
print (nombre_completo2)

texto_largo = """
Selecciona una opcion
[1] Sopa
[2] Pure de calabaza
[3] postre

"""

opcion = input(texto_largo)
print(f'la opcion es {opcion}')

