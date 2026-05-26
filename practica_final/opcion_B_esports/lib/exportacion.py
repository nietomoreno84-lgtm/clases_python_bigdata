import csv
import os
from openpyxl import Workbook, load_workbook



def crear_csv(lista, nombre, carpeta):
    fichero = open(f"./{carpeta}/{nombre}", 'a', encoding='UTF-8', newline='')
    # saber las cabeceras.
    cabeceras = []
    for key in lista[0].keys():
        cabeceras.append(key)
    #volcar los datos de la lista en un objeto csv
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras) 
    #imprimir cabeceras en la primera linea
    mi_csv.writeheader()
    # Escribir cada fila en el csv
    mi_csv.writerows(lista)
    # cerramos el fichero
    fichero.close()


def crear_excel(carpeta, fichero, datos, hoja):
    ruta = f"./{carpeta}/{fichero}"
    if os.path.exists(ruta):
    # Cargarlo si existe
        wb = load_workbook(ruta)
    else:
        # Crear uno nuevo si no existe
        wb = Workbook()
    
    ws =  wb.create_sheet(title=hoja)
        
       
        # crear primero el libro de excel
        
    # extraer de un diccionario cualquier de mi lista las cabeceras.
    cabeceras = list(datos[0].keys())
    # quiero añadirlo a mi hoja
    ws.append(cabeceras)
    
    # recorremos nuestra de lista de datos para imprimir en cada fila un dato concreto
    for item in datos:
        # para que esto funcione el empleado tiene que tener los datos en el mismo orden que la lista caberas. Y estar convertido en lista.
        # lista_empleado = list(empleado.values())
        lista_item = [item[clave] for clave in cabeceras ]
        ws.append(lista_item)
    
    wb.save(f'./{carpeta}/{fichero}')
