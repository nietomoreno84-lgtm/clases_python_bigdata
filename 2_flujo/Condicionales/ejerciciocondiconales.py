"""

    Cálculo del precio a pagar en un aparcamiento
    - Pedir el número de horas que ha estado aparcado (número decimales permitidos)
        - El número de horas debe ser mayor de 0
    - Pedir si tiene tarjeta residente o no ("s" o "n")
        - La opción solo puede ser s o n
    - Pedir el tipo de vehículo ("moto", "coche", "furgoneta")
        - El tipo de vehículo debe ser moto, coche o furgonet
    - Validamos los datos

    - Cálculo el precio dependiendo de las horas:
        - Primera hora: 2€
        - De 1 a 3 horas: 1.5€ por hora adicional
        - Más de 3 horas: 1€ por hora adicional a partir de la 3ª

"""

# Pedir datos
horas = float(input("Introduce las horas usadas: "))
residente = input("¿Tiene tarjeta residente? [s/n]: ")
vehiculo = input("Tipo de vehículo [moto/coche/furgoneta]: ")

# Validación
if horas <= 0:
    print("el numero de horas debe ser mayor que cero")

elif residente != "s" and residente != "n":
    print("la tarjeta debe ser 's' o 'n'")

elif vehiculo != "moto" and vehiculo != "coche" and vehiculo != "furgoneta":
    print("tipo de vehículo no válido")

else:
    # Cálculo del precio
    if horas <= 1:
        precio = 2
    elif horas <= 3:
        precio = 2 + (horas - 1) * 1.5
    else:
        precio = 2 + (2 * 1.5) + (horas - 3)
    
    print(f'has estado {horas} horas. precio a pagar: {precio}€')


     # Multiplicador por vehículo
    if vehiculo == "moto":
        precio = precio * 0.7
    elif vehiculo == "coche":
        precio = precio * 1
    else:
        precio = precio * 1.5

    precio_base = precio

    # Descuento residente
    if residente == "s":
        descuento = precio_base * 0.2
    else:
        descuento = 0

    total = precio_base - descuento

    # Mostrar ticket
    if residente == "s":
        texto_residente = "sí"
    else:
        texto_residente = "no"

    print("--- TICKET DE APARCAMIENTO ---")
    print("Horas:", horas, "| Vehículo:", vehiculo, "| Residente:", texto_residente)
    print("Precio base:", round(precio_base, 2), "€")
    print("Descuento residente:", "-", round(descuento, 2), "€")
    print("TOTAL:", round(total, 2), "€")