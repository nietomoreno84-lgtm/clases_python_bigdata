def limpiar_texto(valor, mayusculas = False):
    if not valor:
        return 'Sin datos'
    valor = str(valor).strip()
    return valor.upper() if mayusculas else valor.lower()
