import csv
from lib.limpieza import normalizar_texto
from lib.limpieza import limpiar_valor_numerico
from openpyxl import Workbook

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
    """
    Procesa y limpia una lista de jugadores.

    La función recorre una lista de diccionarios con información de jugadores
    y normaliza los datos de texto y numéricos para generar una nueva lista
    con información limpia y estandarizada.

    Parámetros:
        lista (list[dict]): Lista de diccionarios que contiene información
                            de jugadores.

    Retorna:
        list[dict]: Nueva lista con los datos de los jugadores procesados.

    Funcionamiento:
        - Recorre cada elemento de la lista original.
        - Normaliza los campos de texto mediante `normalizar_texto()`.
        - Limpia los valores numéricos mediante `limpiar_valor_numerico()`.
        - Genera un nuevo diccionario con los datos transformados.
        - Añade cada jugador procesado a una nueva lista.
        - Devuelve la lista final limpia.

    Campos procesados:
        - id_jugador
        - gamertag
        - nombre_real
        - edad
        - pais
        - equipo
        - rol
        - salario_mensual

    Ejemplo:
        >>> jugadores = [
        ...     {
        ...         'id_jugador': ' jp01 ',
        ...         'gamertag': 'Shadow',
        ...         'nombre_real': 'juan perez',
        ...         'edad': '22',
        ...         'pais': 'españa',
        ...         'equipo': 'dragons',
        ...         'rol': 'support',
        ...         'salario_mensual': '2500'
        ...     }
        ... ]

        >>> procesar_jugadores(jugadores)

        [
            {
                'id_jugador': 'Jp01',
                'gamertag': 'Shadow',
                'nombre_real': 'Juan perez',
                'edad': 22,
                'pais': 'España',
                'equipo': 'Dragons',
                'rol': 'Support',
                'salario_mensual': 2500
            }
        ]

    Requisitos:
        - Deben existir previamente las funciones:
              - `normalizar_texto()`
              - `limpiar_valor_numerico()`
        - Cada diccionario debe contener todas las claves esperadas.

    Excepciones:
        KeyError:
            Se produce si falta alguna clave en los diccionarios de entrada.
        ValueError:
            Puede producirse si un valor numérico no puede convertirse correctamente.

    Notas:
        - La función no modifica la lista original.
        - Devuelve una nueva lista con datos normalizados.
    """
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
    """
    Procesa y limpia una lista de partidas.

    La función recorre una lista de diccionarios con información de partidas
    y normaliza los datos de texto y numéricos para generar una nueva lista
    con información limpia y estandarizada.

    Parámetros:
        lista (list[dict]): Lista de diccionarios que contiene información
                            de partidas.

    Retorna:
        list[dict]: Nueva lista con los datos de las partidas procesados.

    Funcionamiento:
        - Recorre cada elemento de la lista original.
        - Normaliza los campos de texto mediante `normalizar_texto()`.
        - Limpia los valores numéricos mediante `limpiar_valor_numerico()`.
        - Mantiene el campo `fecha` sin modificaciones.
        - Genera un nuevo diccionario con los datos transformados.
        - Añade cada partida procesada a una nueva lista.
        - Devuelve la lista final limpia.

    Campos procesados:
        - id_partida
        - fecha
        - equipo_1
        - equipo_2
        - puntuacion_1
        - puntuacion_2
        - mapa
        - torneo
        - duracion_minutos

    Ejemplo:
        >>> partidas = [
        ...     {
        ...         'id_partida': ' p001 ',
        ...         'fecha': '2026-05-20',
        ...         'equipo_1': 'dragons',
        ...         'equipo_2': 'titans',
        ...         'puntuacion_1': '16',
        ...         'puntuacion_2': '12',
        ...         'mapa': 'inferno',
        ...         'torneo': 'masters league',
        ...         'duracion_minutos': '45'
        ...     }
        ... ]

        >>> procesar_partidas(partidas)

        [
            {
                'id_partida': 'P001',
                'fecha': '2026-05-20',
                'equipo_1': 'Dragons',
                'equipo_2': 'Titans',
                'puntuacion_1': 16,
                'puntuacion_2': 12,
                'mapa': 'Inferno',
                'torneo': 'Masters league',
                'duracion_minutos': 45
            }
        ]

    Requisitos:
        - Deben existir previamente las funciones:
              - `normalizar_texto()`
              - `limpiar_valor_numerico()`
        - Cada diccionario debe contener todas las claves necesarias.

    Excepciones:
        KeyError:
            Se produce si falta alguna clave en los datos de entrada.
        ValueError:
            Puede producirse si un valor numérico no puede convertirse correctamente.

    Notas:
        - La función no modifica la lista original.
        - Devuelve una nueva lista con los datos normalizados.
        - El campo `fecha` se conserva tal como aparece en los datos originales.
    """
    lista_limpia = []
    for item in lista:
       item_limpio = {
           'id_partida': normalizar_texto(item['id_partida']),
           'fecha':item['fecha'],
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
    """
    Procesa y limpia una lista de premios de torneos.

    La función recorre una lista de diccionarios con información de premios
    y normaliza los datos de texto y numéricos para generar una nueva lista
    con información limpia y estandarizada.

    Parámetros:
        lista (list[dict]): Lista de diccionarios que contiene información
                            sobre premios y resultados de torneos.

    Retorna:
        list[dict]: Nueva lista con los datos de premios procesados.

    Funcionamiento:
        - Recorre cada elemento de la lista original.
        - Normaliza los campos de texto mediante `normalizar_texto()`.
        - Limpia los valores numéricos mediante `limpiar_valor_numerico()`.
        - Genera un nuevo diccionario con los datos transformados.
        - Añade cada elemento procesado a una nueva lista.
        - Devuelve la lista final limpia.

    Campos procesados:
        - torneo
        - edicion
        - equipo
        - posicion
        - premio_eur
        - fecha

    Ejemplo:
        >>> premios = [
        ...     {
        ...         'torneo': 'masters cup',
        ...         'edicion': '2025',
        ...         'equipo': 'dragons',
        ...         'posicion': '1',
        ...         'premio_eur': '50000',
        ...         'fecha': '20250510'
        ...     }
        ... ]

        >>> procesar_premios(premios)

        [
            {
                'torneo': 'Masters cup',
                'edicion': '2025',
                'equipo': 'Dragons',
                'posicion': 1,
                'premio_eur': 50000,
                'fecha': 20250510
            }
        ]

    Requisitos:
        - Deben existir previamente las funciones:
              - `normalizar_texto()`
              - `limpiar_valor_numerico()`
        - Cada diccionario debe contener todas las claves necesarias.

    Excepciones:
        KeyError:
            Se produce si falta alguna clave en los datos de entrada.
        ValueError:
            Puede producirse si un valor numérico no puede convertirse correctamente.

    Notas:
        - La función no modifica la lista original.
        - Devuelve una nueva lista con datos normalizados.
        - El campo `fecha` es tratado como valor numérico mediante
          `limpiar_valor_numerico()`.
    """

    lista_limpia = []
    for item in lista:
       item_limpio = {
           'torneo': normalizar_texto(item['torneo']),
           'edicion': normalizar_texto(item['edicion']),
           'equipo': normalizar_texto(item['equipo']),
           'posicion': limpiar_valor_numerico(item['posicion']),
           'premio_eur': limpiar_valor_numerico(item['premio_eur']),
            'fecha': limpiar_valor_numerico(item['fecha']),
             }
       lista_limpia.append(item_limpio)
    return lista_limpia





# def cuantificacion_correciones(equipos_sucios, equipos_limpios):
  
def cuantificacion_correciones(lista_sucia, lista_limpia):
    """
    Cuenta la cantidad de cambios realizados entre una lista original
    y una lista limpia de datos.

    La función compara automáticamente cada celda de ambas listas
    utilizando las columnas detectadas en el primer registro.
    Está diseñada para funcionar con cualquier fichero de datos
    de la CyberLeague sin necesidad de especificar manualmente
    las columnas.

    Parámetros:
        lista_sucia (list[dict]):
            Lista original con los datos sin procesar.

        lista_limpia (list[dict]):
            Lista con los datos ya limpiados y normalizados.

    Retorna:
        int:
            Número total de cambios detectados entre ambas listas.

    Funcionamiento:
        - Comprueba si alguna lista está vacía.
        - Extrae automáticamente las columnas del primer registro.
        - Recorre fila por fila ambas listas.
        - Compara cada valor original con el valor limpio.
        - Incrementa un contador cuando detecta diferencias.
        - Devuelve el total de cambios encontrados.

    Ejemplo:
        >>> lista_sucia = [
        ...     {'nombre': ' JUAN ', 'edad': '20'},
        ...     {'nombre': 'ana', 'edad': '25'}
        ... ]

        >>> lista_limpia = [
        ...     {'nombre': 'Juan', 'edad': 20},
        ...     {'nombre': 'Ana', 'edad': 25}
        ... ]

        >>> cuantificacion_correciones(lista_sucia, lista_limpia)

        3

    Requisitos:
        - Ambas listas deben contener diccionarios con las mismas claves.
        - Las listas deben tener la misma estructura y cantidad de elementos.

    Excepciones:
        KeyError:
            Puede producirse si alguna clave no existe en ambas listas.
        IndexError:
            Puede producirse si las listas tienen tamaños diferentes.

    Notas:
        - La función compara los valores usando `!=`.
        - Las columnas se detectan automáticamente a partir
          del primer elemento de `lista_sucia`.
        - Si alguna lista está vacía, la función devuelve `0`.
        - Es una función genérica reutilizable para distintos tipos
          de datasets de la CyberLeague.
    """

    # Si alguna lista viene vacía o no hay datos, no hay cambios que contar
    if not lista_sucia or not lista_limpia:
        return 0
        
    contador_cambios = 0     
    
    # Extrae las columnas automáticas del primer registro del fichero actual
    columnas = list(lista_sucia[0].keys()) 
    
    # Recorremos fila por fila
    for i in range(len(lista_limpia)):
        # Recorremos cada columna de esa fila de forma automática
        for col in columnas:
    #         # Comparamos si el valor original es diferente al limpio
             if lista_sucia[i][col] != lista_limpia[i][col]:
                 contador_cambios += 1
                
    return contador_cambios


def hacer_auditoria(lista_registros, nombre_fichero):
    """
    Realiza una auditoría básica de calidad sobre un conjunto de registros.

    La función analiza automáticamente una lista de diccionarios y genera
    un informe con métricas de calidad de datos, incluyendo:
    - Valores vacíos
    - Registros duplicados
    - Espacios extra en los textos
    - Estructuras preparadas para formatos inconsistentes y valores fuera de rango

    Está diseñada para funcionar de forma genérica con cualquier fichero
    de la CyberLeague.

    Parámetros:
        lista_registros (list[dict]):
            Lista de registros que se desean auditar.

        nombre_fichero (str):
            Nombre del fichero auditado.
            Actualmente no se utiliza dentro de la función, pero puede
            emplearse para informes o trazabilidad futura.

    Retorna:
        dict:
            Diccionario con el resumen de la auditoría.

            Estructura del resultado:

            {
                "total_registros": int,
                "valores_vacios": dict,
                "duplicados": int,
                "formatos_inconsistentes": dict,
                "fuera_de_rango": dict,
                "espacios_extra": dict
            }

    Funcionamiento:
        - Comprueba si la lista está vacía.
        - Detecta automáticamente las columnas usando el primer registro.
        - Cuenta el número total de registros.
        - Detecta registros duplicados exactos.
        - Cuenta valores vacíos o equivalentes.
        - Detecta espacios innecesarios en los textos.
        - Inicializa estructuras para futuros controles de calidad.

    Controles realizados:
        1. Valores vacíos:
            Considera vacíos los siguientes valores:
            - ""
            - "n/a"
            - "-"
            - "no disponible"
            - "null"
            - "none"
            - None

        2. Duplicados:
            Detecta registros idénticos comparando todos sus campos.

        3. Espacios extra:
            Detecta:
            - Espacios al inicio o final.
            - Dobles espacios internos.

    Ejemplo:
        >>> registros = [
        ...     {
        ...         "nombre": " Juan ",
        ...         "equipo": "Dragons",
        ...         "pais": "España"
        ...     },
        ...     {
        ...         "nombre": "Juan",
        ...         "equipo": "Dragons",
        ...         "pais": "España"
        ...     }
        ... ]

        >>> hacer_auditoria(registros, "jugadores.csv")

        {
            'total_registros': 2,
            'valores_vacios': {
                'nombre': 0,
                'equipo': 0,
                'pais': 0
            },
            'duplicados': 0,
            'formatos_inconsistentes': {
                'nombre': [],
                'equipo': [],
                'pais': []
            },
            'fuera_de_rango': {
                'nombre': 0,
                'equipo': 0,
                'pais': 0
            },
            'espacios_extra': {
                'nombre': 1,
                'equipo': 0,
                'pais': 0
            }
        }

    Requisitos:
        - La lista debe contener diccionarios homogéneos.
        - Todos los registros deben compartir las mismas columnas.

    Excepciones:
        AttributeError:
            Puede producirse si algún registro no es un diccionario.
        TypeError:
            Puede producirse si `lista_registros` no es iterable.

    Notas:
        - La función es completamente genérica y reutilizable.
        - Los campos `formatos_inconsistentes` y `fuera_de_rango`
          están preparados para futuras validaciones avanzadas.
        - Si la lista está vacía, devuelve una auditoría vacía
          con valores inicializados.
    """

    
    if not lista_registros:
        return {
            "total_registros": 0,
            "valores_vacios": {},
            "duplicados": 0,
            "formatos_inconsistentes": {},
            "fuera_de_rango": {},
            "espacios_extra": {}
        }

    # Extraemos las columnas automáticamente mirando el primer registro
    columnas = list(lista_registros[0].keys()) if isinstance(lista_registros, list) and lista_registros else []

    resultado = {
        "total_registros": len(lista_registros),
        "valores_vacios": {col: 0 for col in columnas},
        "duplicados": 0,
        "formatos_inconsistentes": {col: [] for col in columnas},
        "fuera_de_rango": {col: 0 for col in columnas},
        "espacios_extra": {col: 0 for col in columnas}
    }

    filas_vistas = []
    valores_vacio = ["", "n/a", "-", "no disponible", "null", "none"]

    for registro in lista_registros:
        # Control de Duplicados Exactos
        fila_str = str(sorted(registro.items()))
        if fila_str in filas_vistas:
            resultado["duplicados"] += 1
        else:
            filas_vistas.append(fila_str)
            
        # Control de campos (vacíos y espacios)
        for col in columnas:
            valor = registro.get(col, "")
            valor_str = str(valor)
            
            if valor is None or valor_str.strip().lower() in valores_vacio or valor_str == "":
                resultado["valores_vacios"][col] += 1
                continue
                
            if valor_str != valor_str.strip() or "  " in valor_str:
                resultado["espacios_extra"][col] += 1

    return resultado







