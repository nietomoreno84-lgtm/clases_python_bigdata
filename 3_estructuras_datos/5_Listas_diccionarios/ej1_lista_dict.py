# quiero un menu cli, 2 opciones insertar contacto y salir
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir
contactos = []

def insertar_contacto(nombre, tlf, lista):
    pass


def main():
    menu = """## Bienvenido a la agenda de contactos ##
[1]. Insertar un contacto
[x]. Salir de la app
"""
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        nombre = input('Dime el nombre del contacto: ')
        telefono = input('Teléfono')
        insertar_contacto(nombre, telefono, contactos)
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()

main()

