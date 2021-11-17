
tu_numero = input('Por favor, introduce un número: ')
numero = int(tu_numero)

if( numero % 2 == 0):
    print('El número', numero, 'es par')
    if( numero % 4 == 0):
        print('y también es múltiplo de 4')
else:
    print('El número', numero, 'es impar')
