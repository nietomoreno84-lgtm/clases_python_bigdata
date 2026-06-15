   # visualizar datos de forma fácil con pandas
import pandas as pd
from db.config import get_connection
from mysql.connector import Error
from colorama import init, Fore, Style
from tabulate import tabulate


# Inicializar colorama
init(autoreset=True)

def get_compra():
    try:
        # cramos la conexion con conn
        conn = get_connection()
        #abrimos el sqlfile para hacer la consulta sql
        cursor = conn.cursor(dictionary=True)
        # HAcemos la consulta SQL
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return[]
    finally:
        conn.close()


def aplicar_color(prioridad):
    prioridad = prioridad.lower()
    if prioridad == 'alta':
        return f"{Fore.RED}{prioridad}{Style.RESET_ALL}"
    elif prioridad == 'media':
        return f"{Fore.YELLOW}{prioridad}{Style.RESET_ALL}"
    elif prioridad == 'baja':
        return f"{Fore.GREEN}{prioridad}{Style.RESET_ALL}"
    return prioridad


def pintar_compra(lista):
    if not lista or len(lista) == 0:
        print('No necesitamos nada, lista vacia')

    df = pd.DataFrame(lista)
    # voy a aplicar solo a la columna prioridad el color segun el texto almacenado

    if 'prioridad' in df.columns:
        df['prioridad'] = df['prioridad'].apply(aplicar_color)

    # añadir directamente a mi df una columna nueva
    df['precio_total'] = df['precio'] * df['cantidad'] * 1.21


    print('-' * 30)
    print('# Lista Productos #')
    # header='keys' muestra el nombre de las columnas y showindex=False quita la posicion del dataframe
    print(tabulate(df,headers='keys', showindex=False))
    print('-' * 30)


def eliminar_articulo(id):
    # obtener la conexion
    try:
        # cramos la conexion con conn
        conn = get_connection()
        #abrimos el sqlfile para hacer la consulta sql
        cursor = conn.cursor()
        # HAcemos la consulta SQL
        cursor.execute('delete from productos where id=%s',(id,))
        conn.commit()

        if cursor.rowcount > 0:
            return f'el producto con id {id} ha sido eliminado'
        return 'no se ha podido eliminar el producto, id no encontrado'  
    except Error as e:
        print(f"Error: {e}")
        return[]
    finally:
        conn.close()