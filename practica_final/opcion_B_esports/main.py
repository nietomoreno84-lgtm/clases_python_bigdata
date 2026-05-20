from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
from lib.limpieza import limpiar_texto


fichero = 'equipos.xlsx'
equipos = cargar_excel('datos', fichero)
print('Numero total de registros:', len(equipos))
print('Nombre del fichero', fichero)
print('Nombre de los campos:', list(equipos[0].keys()))
for i in range(len(equipos)):
    print(equipos[i]['nombre_equipo'])
    if i == 5:
        break

# for equipo in equipos:
#     nombre = limpiar_texto(equipo['nombre_equipo'], True)
#     region = limpiar_texto(equipo['region'])
#     precio = limpiar_texto
#     print(nombre, region)


