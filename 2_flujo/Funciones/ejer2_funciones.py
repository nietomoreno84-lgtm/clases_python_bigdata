input("numero_1", "numero_2" , numero_3):

def sumar(n1,n2,n3):
    return n1 + n2 + n3

def dividir(divisor, dividendo):
    return divisor / dividendo

def media(numero_1, numero_2, numero_3):
    suma = sumar(numero_1, numero_2, numero_3)
    media = dividir(suma, 3)
    print(media)

numero_1 = float(input ('dame un numero'))
numero_2 = float(input ('dame un numero'))
numero_3 = float(input ('dame un numero'))

media(2,3,5)