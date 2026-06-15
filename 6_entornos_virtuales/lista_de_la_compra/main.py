
# nos traemos cada una de la funciones que me permitan conectarme con los datos
from controllers.consultas_controller import get_compra, pintar_compra,eliminar_articulo

def init():
    menu = """##### Lista de compra #####
    [1]. Añadir articulo
    [2]. Eliminar articulo
    [3]. Ver la lista de la compra
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        try:
            nombre = input ('introduce el nombre del producto: ')
            precio =float(input('introduce el precio del producto: '))
            cantidad = int(input('introduce la cantidad del producto: '))
            prioridad = input('introduce la prioridad , alta , media, baja: ')
            
        except ValueError:
            print ('Precio y cantidad tienen que ser numeros')    
    elif option == '2':
        id = input('dame el id del articulo  eliminar')
        result = eliminar_articulo(int(id))
        print(result)
    elif option == '3':
        result = get_compra()
        pintar_compra(result)
    elif option.lower() == 'x':
        print('Hasta pronto')
        return False
    else:
        print('No es una opcion valida')
    init()



if __name__ == "__main__":
    init()
    