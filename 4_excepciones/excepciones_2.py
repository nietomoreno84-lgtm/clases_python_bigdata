
try:
    numero = int(input('dime un numero : '))
    numero2 = int(input('dime otro numero : '))
    resultado = numero/numero2
    print(resultado)
except ValueError:
    print('los valores no son numeros: ')
except ZeroDivisionError:    
    print('no se puede dividir por cero')
except: 
    print('futuro error no previsto')  

print('otros calculos')
