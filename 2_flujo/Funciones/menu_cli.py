## vamos a crear un menu, que me permita decidir que operacion va hacer mi calculadora. 

def main():
    menu = """
## BIENVENIDO A NUESTRA MARAVILLOSA CALCULADORA ##
--------------------------------------------------
[1] Sumar
[2] Restar
[3] Multiplicar
[x] Salir   
"""
    print(menu)
    option = input('¿Que operación quieres realizar? ')
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == 'x':
        print('Hasta pronto, vuelve cuando quieras')
    else:
        print('valor introducido no valido')
    
main()