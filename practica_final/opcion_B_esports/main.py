from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
from lib.limpieza import limpiar_texto
from lib.limpieza import normalizar_texto, mapeo_equipo, mapeo_master
from lib.limpieza import limpiar_valor_numerico
from lib.auditoria import procesar_equipo
from lib.auditoria import procesar_premios
from lib.auditoria import procesar_partidas
from lib.auditoria import procesar_jugadores
from lib.auditoria import cuantificacion_correciones

premios_sucio= cargar_csv('datos', 'premios.csv')
partidas_sucios = cargar_json('datos', 'partidas.json')
jugadores_sucios = cargar_csv('datos','jugadores.csv')






#  PROCESAR 1 HOJA (Hoja activa)
print("\n--- Cargando 1 Hoja: EQUIPOS ---")
equipos_sucios = cargar_excel('datos', 'equipos.xlsx')
equipos_limpios = procesar_equipo(equipos_sucios)


# # Limpiamos la hoja 1 por fila
# for equipo in equipos_sucios:
#     nombre = normalizar_texto(equipo['nombre_equipo'])
#     anio_fundacion = normalizar_texto(equipo['anio_fundacion'])
#     region = limpiar_texto(equipo['region'])
#     presupuesto_anual = limpiar_valor_numerico(equipo['presupuesto_anual'])
#     sede = normalizar_texto(equipo['sede'])
#     print(f"Equipo: {nombre} | Sede: {sede} | Presupuesto: {presupuesto_anual}")


# # Procesar Hoja Staff (Hoja 2)
# print("\n--- CARGANDO HOJA 2: STAFF ---")
# staff = cargar_excel('datos', 'equipos.xlsx', hoja2='staff')

# # Limpiamos la hoja 2
# for miembro in staff:
#     equipo_limpio = normalizar_texto(miembro['equipo'])
#     nombre_limpio = normalizar_texto(miembro['nombre'])
#     cargo_limpio = limpiar_texto(miembro['cargo'])
#     email_limpio = limpiar_texto(miembro['email'])
#     telefono_limpio = limpiar_valor_numerico(miembro['telefono'])
#     print(f"Equipo: {equipo_limpio} | Miembro: {nombre_limpio} | Cargo: {cargo_limpio}")







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
# premios_limpio =procesar_premios(premios_sucio)
# partidas_limpio = procesar_partidas(partidas_sucios)
# jugadores_limpio = procesar_jugadores(jugadores_sucios)
# print(partidas_limpio)
# print(jugadores_limpio)
# print(partidas_limpio)
# print(premios_limpio)


numero_correciones = cuantificacion_correciones(equipos_sucios, equipos_limpios)
print(numero_correciones)
mapeo_equipo(equipos_limpios, mapeo_master )
