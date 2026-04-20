nota = float(input('dime tu nota'))


if nota >= 5 and nota <= 10:
    print( 'estas aprobado')
elif nota >= 0 and nota < 5:
    print('estas suspenso')
else:
    print('la nota no es correcta')



if 0 <= nota < 5: 
    print( 'suspenso')
elif 5<= nota <6:
    print('sufieciente')
elif 6<= nota <7:
    print('bien')
elif 7<= nota <9:
    print('notable')
elif 9<= nota <=10:
    print('sobresaliente')
else : 
    print('nota no es correcta')

    
