import os
from functions import *
from classes import *

while True:
    os.system('cls')
    print('Aplicación para ver gráficos sobre la pandemia del Covid')
    print('¿Qué gráfica quieres visualizar')
    print('1. Defunciones')
    print('2. Casos')
    print('3. Hospitalizaciones')
    print('4. UCI')
    print('5. Salir')
    try:
        option = int(input(''))
        data = get_data()
        if(option < 5):
            select_options(option, data)
            continue
        elif(option == 5):
            print('Gracias por usar la aplicación')
            reset()
            break
        else:
            print('Por favor, escoge una opción del 1 al 5')
            reset()
            continue
    except DataFileError as error:
        print(error)
        reset()
    except ValueError as error:
        print('Por favor inserta un valor con carácter numérico')
        reset()
    except CustomError as error:
        print(error)
        reset()
    except Exception as error:
        print(error)
        reset()



    