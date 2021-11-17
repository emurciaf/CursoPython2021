import datetime

def obtener_cuando100(tu_edad, ano_actual):
    if( int(tu_edad) >= 100):
        ano_100 = ano_actual
    else :
        ano_100 = ano_actual + 100 - int(tu_edad)
    return ano_100


ano_actual = datetime.date.today().year

tu_nombre = input('Por favor, introduce tu nombre: ')
tu_edad = input('Dime tu edad: ')
tus_100 = obtener_cuando100( tu_edad, ano_actual)

if( tus_100 == ano_actual):
    print('Hola', tu_nombre, ', ya tienes 100 años')
else:
    print('Hola', tu_nombre, ', cumples 100 años en el año', tus_100)
