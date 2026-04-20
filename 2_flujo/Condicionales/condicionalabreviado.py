# Definir el valor de una variable en funcion de una condicion

estado_luz = True

if estado_luz:
    mensaje = "la luz esta encendida"
else:
    mensaje = "la luz esta apagada"    

mensaje = "luz encendida" if estado_luz else "luz apagada"   

print(mensaje)