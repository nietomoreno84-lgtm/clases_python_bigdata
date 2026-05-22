from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
# from lib.limpieza import limpiar_texto
# from lib.limpieza import normalizar_texto
# from lib.limpieza import limpiar_valor_numerico
from lib.auditoria import procesar_equipo
from lib.auditoria import procesar_premios
from lib.auditoria import procesar_partidas
from lib.auditoria import procesar_jugadores

premios_sucio= cargar_csv('datos', 'premios.csv')
partidas_sucios = cargar_json('datos', 'partidas.json')
jugadores_sucios = cargar_csv('datos','jugadores.csv')
equipos_sucios = cargar_excel('datos', 'equipos.xlsx')
# partidas = cargar_json('datos', 'partidas.json')
# jugadores = cargar_csv('datos','jugadores.csv')
# premios = cargar_csv('datos', 'premios.csv')

# cargar_json('datos','partidas.json')


# for equipo in equipos:
#     nombre = limpiar_texto(equipo['nombre_equipo'], True)
#     region = limpiar_texto(equipo['region'])
#     sede = limpiar_texto(equipo['sede'])
#     presupuesto = limpiar_valor_numerico(equipo['presupuesto_anual'])
#     print(nombre, region , sede, presupuesto, )
 


# prueba de acentos 
# texto_limpio = limpiar_texto('   daviD   ', True)
# print(texto_limpio)

# 
equipos_limpios =procesar_equipo(equipos_sucios)
premios_limpio =procesar_premios(premios_sucio)
partidas_limpio = procesar_partidas(partidas_sucios)
jugadores_limpio = procesar_jugadores(jugadores_sucios)
print(partidas_limpio)
# print(jugadores_limpio)
# print(partidas_limpio)
# print(premios_limpio)