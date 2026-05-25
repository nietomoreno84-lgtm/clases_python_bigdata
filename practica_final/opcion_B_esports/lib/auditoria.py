
from lib.limpieza import normalizar_texto
from lib.limpieza import limpiar_valor_numerico



def procesar_equipo(lista):
    ## recorrer la lista y limpiar cada elemento de la lista. El objetivo de esta funcion es recibir una lista de datos sucia y devolverla limpia.
    lista_limpia = []
    for item in lista:
       item_limpio = {
      
           'presupuesto_anual': limpiar_valor_numerico(item['presupuesto_anual']),
           'nombre_equipo' : normalizar_texto(item['nombre_equipo']),
           'region': normalizar_texto(item['region']),
           'sede': normalizar_texto(item['sede']),
           'anio_fundacion':item['anio_fundacion']
       }
       lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_jugadores(lista):
    lista_limpia = []
    for item in lista:
       item_limpio = {
           'id_jugador': normalizar_texto(item['id_jugador']),
           'gamertag' : normalizar_texto(item['gamertag']),
           'nombre_real': normalizar_texto(item['nombre_real']),
           'edad': limpiar_valor_numerico(item['edad']),
           'pais': normalizar_texto(item['pais']),
            'equipo': normalizar_texto(item['equipo']),
            'rol': normalizar_texto(item['rol']),
            'salario_mensual': limpiar_valor_numerico(item['salario_mensual']),


       }
       lista_limpia.append(item_limpio)
    return lista_limpia

def procesar_partidas(lista):
    lista_limpia = []
    for item in lista:
       item_limpio = {
           'id_partida': normalizar_texto(item['id_partida']),
           'equipo_1': normalizar_texto(item['equipo_1']),
           'equipo_2': normalizar_texto(item['equipo_2']),
           'puntuacion_1': limpiar_valor_numerico(item['puntuacion_1']),
            'puntuacion_2': limpiar_valor_numerico(item['puntuacion_2']),
            'mapa': normalizar_texto(item['mapa']),
            'torneo': normalizar_texto(item['torneo']),
            'duracion_minutos' : limpiar_valor_numerico(item['duracion_minutos'])
             }
       lista_limpia.append(item_limpio)
    return lista_limpia



def procesar_premios(lista):
    lista_limpia = []
    for item in lista:
       item_limpio = {
           'torneo': normalizar_texto(item['torneo']),
           'edicion': normalizar_texto(item['edicion']),
           'equipo': normalizar_texto(item['equipo']),
           'posicion': limpiar_valor_numerico(item['posicion']),
            'premio_eur': limpiar_valor_numerico(item['premio_eur']),
          
             }
       lista_limpia.append(item_limpio)
    return lista_limpia





def cuantificacion_correciones(equipos_sucios, equipos_limpios):
  

    # equipos_sucios y equipos_limpios es una lista de diccionarios
    # como se recorre una lista
    contador_cambios =0     
    for i in range(len(equipos_sucios)):
        if equipos_sucios[i]['nombre_equipo'] != equipos_limpios[i]['nombre_equipo']:
            contador_cambios += 1
        if equipos_sucios[i]['region'] != equipos_limpios[i]['region']:
            contador_cambios += 1 
        if equipos_sucios[i]['anio_fundacion'] != equipos_limpios[i]['anio_fundacion']:
            contador_cambios += 1
        if equipos_sucios[i]['presupuesto_anual'] != equipos_limpios[i]['presupuesto_anual']:
            contador_cambios += 1
        if equipos_sucios[i]['sede'] != equipos_limpios[i]['sede']:
            contador_cambios += 1
    return(contador_cambios)