import mysql.connector
from mysql.connector import Error

#  configurar nuestra conexion

DB_CONFIG= {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'David1984..',
    'database' : 'tinta_eterna'
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f'error: {e}')
        return None
    
# listado con todos los libros

def get_all_books():
    try:
    # lo primero sera conectarse a la bbdd
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from libros')
        return cursor.fetchall()
    except Error as e:
        print(f'error: {e}')    
        return []
    finally:
        conn.close()

# libros = get_all_books()
# print(libros)


# voy hacer una peticion de un libro por id

def get_book_by_id(id_libro):
    try:
    # lo primero sera conectarse a la bbdd
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'select * from libros where id=%s',(id_libro,))


        return cursor.fetchone()
    except Error as e:
        print(f'error: {e}')    
        return None
    finally:
        conn.close()


libro_1= get_book_by_id(1)
print(libro_1)