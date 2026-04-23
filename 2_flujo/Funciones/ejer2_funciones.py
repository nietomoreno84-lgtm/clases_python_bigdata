numero_1 = float(input('Dame el número: '))
numero_2 = float(input('Dame el número: '))
numero_3 = float(input('Dame el número: '))
def sumar(n1,n2,n3):
    return n1 + n2 +n3


def dividir(divisor, dividendo):
    return divisor / dividendo

def media(numero_1, numero_2, numero_3):
    suma = (numero_1 + numero_2 + numero_3)
    resultado = dividir(suma, 3)
    print(resultado)

media(numero_1, numero_2, numero_3)