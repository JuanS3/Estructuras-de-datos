from copy import deepcopy


def menu():
    print('-----------------------------------------------------------------------------------')
    print('-                               Examen INTER 2024-1                               -')
    print('-----------------------------------------------------------------------------------')
    print('Escriba el comando C# para indicar la direccion y el numero de casillas a mover')
    print('C coresponde a la direccion (U, D, L, R)')
    print('    U: Arriba')
    print('    D: Abajo')
    print('    L: Izquierda')
    print('    R: Derecha')
    print('# corresponde al numero de casillas a mover')
    print('Ejemplo: U3, D2, L1, R4')
    print('-----------------------------------------------------------------------------------')
    print('Para imprimir el mapa escriba M')
    print('Para salir del programa escriba S')
    print('-----------------------------------------------------------------------------------')
    print('Ingrese una opción: ', end='')
    opt = input()
    print('-----------------------------------------------------------------------------------')
    return opt


def posicion_s(mapa):
    # Busca la posicion de S en el mapa

    # Recorre las filas del mapa por su indice
    for fila in range(len(mapa)):

        # Recorre las columnas del mapa por su indice
        for columna in range(len(mapa[fila])):

            # Si la celda es igual a S
            if mapa[fila][columna] == 'S':
                # Retorna la posicion de S en el mapa
                return fila, columna

    return None # Si no se encuentra S en el mapa


def actualizar_mapa(old, new):
    # Actualiza el mapa old con el contenido de new
    # Recorre las filas del mapa por su indice
    for fila in range(len(old)):

        # Recorre las columnas del mapa por su indice
        for columna in range(len(old[fila])):

             # Actualiza el contenido de la celda de old con el contenido de la celda de new
            old[fila][columna] = new[fila][columna]


def movimiento(mapa, k, direccion):
    # Busca a S en el mapa y trae la posicion del mismo x: fila, y: columna
    x, y = posicion_s(mapa)
    # Copia del mapa para no modificar el original
    mapa_temp = deepcopy(mapa)
    # Variable para saber si se pudo mover, inicialmente en False
    movimiento_valido = False

    # --------------------------
    # Completar el código
    # --------------------------

    # Si se pudo mover
    if movimiento_valido:
        # Actualiza el mapa
        actualizar_mapa(mapa, mapa_temp)

    imprimir_mapa(mapa)
    return movimiento_valido


def imprimir_mapa(mapa):
    print('\n\n\n')

    # Recorre las filas del mapa por su indice y valor
    for i, fila in enumerate(mapa):

        # Imprime el numero de la fila
        print(f'| {i+1} |', end=' - ')

        # Recorre las columnas del mapa por su valor
        for celda in fila:
            # Imprime el contenido de la celda
            print(celda, end=' ')

        # Imprime el final de la fila y un salto de linea
        print('|')

    print('\n\n\n')

    # Espera a que el usuario presione enter para continuar
    input('Presione enter para continuar...')


def main():

    mapa = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '.', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '.', '.', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '.', '#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', 'E', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

    # Ciclo para infinito para el juego
    while True:

        # Muestra el menu y obtiene la opcion del usuario
        opt = menu()

        # Obtiene la direccion
        direccion = opt[0]

        # Si la opcion es S, sale del juego
        if opt[0].upper() == 'S':
            break # Sale del ciclo

        # Si la opcion es M, imprime el mapa
        elif opt[0].upper() == 'M':
            imprimir_mapa(mapa)
            continue # Continua con la siguiente iteracion del ciclo, no ejecuta el codigo restante

        # Se obtiene el numero de casillas a mover
        k = int(opt[1:])

        # Se realiza el movimiento y verifica si se pudo mover
        if movimiento(mapa, k, direccion):
            # Si se pudo mover imprime el mensaje
            print('Movimiento exitoso')

        # Si no se pudo mover
        else:
            # Imprime el mensaje
            print('Movimiento no valido')


main()
