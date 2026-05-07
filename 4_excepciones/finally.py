print('--simulacion de conexion a BBDD')

conexion_bbdd = False
lista_inexsitente = ['uno' , 'dos']

try: 
    print('1 - conectando a la bbdd')
    conexion_bbdd = True
    print('2 - pedimos los datos de un cliente')
    cliente = lista_inexsitente[2]
    print('cliente encontrado')
except NameError:
    print('la tabla de clientes no exixte')
except IndexError:
    print('el cliente solicitado no existe')
finally:
    print('cierro la conexion')  
    
      
print('lo siguiente')    