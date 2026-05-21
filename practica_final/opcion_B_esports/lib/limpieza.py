



correcciones_tildes = {
    "jose":       "José",      "maria":      "María",
    "garcia":     "García",    "gonzalez":   "González",
    "martinez":   "Martínez",  "lopez":      "López",
    "perez":      "Pérez",     "sanchez":    "Sánchez",
    "gomez":      "Gómez",     "fernandez":  "Fernández",
    "rodriguez":  "Rodríguez", "hernandez":  "Hernández",
    "ramirez":    "Ramírez",   "gutierrez":  "Gutiérrez",
    "giron":       "Girón"
}



def normalizar_texto(texto):
    """
    Normaliza un texto aplicando limpieza, corrección de tildes y formato.

    La función realiza varias transformaciones sobre el texto recibido:
    - Limpia espacios y normaliza el formato utilizando `limpiar_texto()`.
    - Convierte el texto a minúsculas.
    - Corrige palabras según un diccionario de tildes.
    - Reconstruye el texto con la primera letra en mayúscula.

    Parámetros:
        texto (str): Texto que se desea normalizar.

    Retorna:
        str: Texto normalizado y corregido.

    Funcionamiento:
        - Limpia el texto mediante la función `limpiar_texto()`.
        - Convierte todo el texto a minúsculas.
        - Divide el texto en palabras.
        - Comprueba cada palabra en el diccionario `correcciones_tildes`.
        - Sustituye las palabras encontradas por su versión corregida.
        - Une nuevamente las palabras en una sola cadena.
        - Convierte la primera letra del texto a mayúscula.

    Ejemplos:
        Suponiendo el siguiente diccionario:

        >>> correcciones_tildes = {
        ...     "camion": "camión",
        ...     "arbol": "árbol"
        ... }

        >>> normalizar_texto("  CAMION rojo ")
        'Camión rojo'

        >>> normalizar_texto("ARBOL grande")
        'Árbol grande'

    Requisitos:
        - Debe existir previamente:
              - La función `limpiar_texto()`
              - El diccionario `correcciones_tildes`
        - `correcciones_tildes` debe contener pares:
              palabra_sin_tilde -> palabra_corregida

    Excepciones:
        IndexError:
            Puede producirse si el texto resultante está vacío y se intenta
            acceder a `texto[0]`.

    Notas:
        - Solo corrige palabras exactas presentes en el diccionario.
        - La capitalización final afecta únicamente a la primera letra
          del texto completo.
    """
    texto = limpiar_texto(texto)
    texto = texto.lower()
    palabras = texto.split()
    palabras_corregidas = []

    for palabra in palabras:
        if palabra in correcciones_tildes:
            palabras_corregidas.append(correcciones_tildes[palabra])
        else:
            palabras_corregidas.append(palabra)

    texto = " ".join(palabras_corregidas)
    texto = texto[0].upper() + texto[1:]

    return texto




def limpiar_texto(valor, mayusculas = False):
    """
    Limpia y normaliza un texto.

    La función convierte el valor recibido a cadena de texto, elimina
    espacios en blanco al inicio y al final, y transforma el texto
    a mayúsculas o minúsculas según el parámetro indicado.

    Parámetros:
        valor (any): Valor que se desea limpiar y normalizar.
                     Puede ser texto, número u otro tipo de dato.
        mayusculas (bool, opcional):
            - True: convierte el texto a mayúsculas.
            - False: convierte el texto a minúsculas.
            Por defecto es False.

    Retorna:
        str:
            - El texto limpio y transformado.
            - 'Sin datos' si el valor está vacío o es nulo.

    Funcionamiento:
        - Comprueba si el valor existe.
        - Si el valor es vacío o nulo, devuelve `'Sin datos'`.
        - Convierte el valor a tipo `str`.
        - Elimina espacios innecesarios con `strip()`.
        - Convierte el texto a mayúsculas o minúsculas.

    Ejemplos:
        >>> limpiar_texto("  Hola Mundo  ")
        'hola mundo'

        >>> limpiar_texto("  Hola Mundo  ", True)
        'HOLA MUNDO'

        >>> limpiar_texto("")
        'Sin datos'

        >>> limpiar_texto(None)
        'Sin datos'

    Requisitos:
        - No requiere librerías externas.

    Notas:
        - La función admite cualquier tipo de dato como entrada,
          ya que convierte el valor a cadena mediante `str()`.
        - Los espacios al inicio y al final del texto son eliminados.
    """
    if not valor:
        return 'Sin datos'
    valor = str(valor).strip()
    return valor.upper() if mayusculas else valor.lower()



