from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
from lib.auditoria import procesar_equipo, procesar_premios, procesar_partidas, procesar_jugadores
from lib.auditoria import cuantificacion_correciones
from lib.exportacion import crear_csv,crear_excel
from lib.auditoria import hacer_auditoria
from lib.exportacion import generar_informe_txt




premios_sucio= cargar_csv('datos', 'premios.csv')
partidas_sucios = cargar_json('datos', 'partidas.json')
jugadores_sucios = cargar_csv('datos','jugadores.csv')






#  PROCESAR 1 HOJA (Hoja activa)
print("\n--- Cargando 1 Hoja: EQUIPOS ---")
equipos_sucios = cargar_excel('datos', 'equipos.xlsx')

equipos_limpios = procesar_equipo(equipos_sucios)
premios_limpio = procesar_premios(premios_sucio)
jugadores_limpio = procesar_jugadores(jugadores_sucios)
partidas_limpio = procesar_partidas(partidas_sucios)

        
crear_csv(jugadores_limpio, 'jugadores.csv', 'datos_limpios')
crear_csv(equipos_limpios, 'equipos.csv', 'datos_limpios') 
crear_csv(partidas_limpio, 'partidas.csv', 'datos_limpios')
crear_csv(premios_limpio, 'premios.csv', 'datos_limpios')

crear_excel('datos_limpios', 'Datos_completo.xlsx',equipos_limpios,'equipos' )
crear_excel('datos_limpios', 'Datos_completo.xlsx',jugadores_limpio,'jugadores' )
crear_excel('datos_limpios', 'Datos_completo.xlsx',partidas_limpio,'partidas' )
crear_excel('datos_limpios', 'Datos_completo.xlsx',premios_limpio,'premios' )

numero_correciones_equipos = cuantificacion_correciones(equipos_sucios, equipos_limpios)
numero_correciones_jugadores = cuantificacion_correciones(jugadores_sucios,jugadores_limpio)
numero_correciones_partidas = cuantificacion_correciones(partidas_sucios,partidas_limpio)
numero_correciones_premios = cuantificacion_correciones(premios_sucio,premios_limpio)



auditoria_global = {
    "equipos.xlsx": hacer_auditoria(equipos_sucios, "equipos.xlsx"),
    "jugadores.csv": hacer_auditoria(jugadores_sucios, "jugadores.csv"),
    "partidas.json": hacer_auditoria(partidas_sucios, "partidas.json"),
    "premios.csv": hacer_auditoria(premios_sucio, "premios.csv")
}


cambios_totales = {
    "equipos.xlsx (Hoja Equipos)":numero_correciones_equipos ,
    "jugadores.csv (Hoja jugadores)": numero_correciones_jugadores,
    "partidas.json": numero_correciones_partidas,
    "premios.csv": numero_correciones_premios
}



# print(equipos_limpios)
generar_informe_txt(auditoria_global, cambios_totales, "datos_limpios/informe_limpieza.txt")