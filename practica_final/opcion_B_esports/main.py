from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
from lib.limpieza import limpiar_texto
from lib.limpieza import normalizar_texto

equipos = cargar_excel('datos', 'equipos.xlsx')
partidas = cargar_json('datos', 'partidas.json')
jugadores = cargar_csv('datos','jugadores.csv')
premios = cargar_csv('datos', 'premios.csv')

# cargar_json('datos','partidas.json')


for equipo in equipos:
    nombre = limpiar_texto(equipo['nombre_equipo'], True)
    region = limpiar_texto(equipo['region'])
    print(nombre, region)


# prueba de acentos 
# texto_limpio = limpiar_texto('   daviD   ', True)
# print(texto_limpio)

# 
