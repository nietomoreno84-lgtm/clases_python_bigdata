nota = float(input('dime tu nota: '))

if nota >= 0 and nota < 5: 
    print ('suspenso')
    print ('otra cosa')

if nota >= 5 and nota <= 10:
    print ('estas aprobado')

"""
    pide por input el importe de una compra
    si el importe es mayor que 100 muestra el mensaje:
        "aplicamos un 10% de descuento"
    y ademas, mostramos el precio con el descuento aplicado    

"""

precio = float (input('dime el precio:'))

if precio > 100:
    print('aplicamos el 10% de descuento')
    precio_con_descuento = precio * 0.9
    print(f"precio original:{precio}€. precio descuento: {precio_con_descuento}€")
    
