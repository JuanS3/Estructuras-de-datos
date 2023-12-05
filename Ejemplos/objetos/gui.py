from carro import Carro, Posicion

class Tablero:

    def __init__(self,
            dimension: int,
            camino: str = '_',
            carro: str = 'X',
            posicion: Posicion = Posicion(0, 0),
        ):
        self.dimension = dimension
        self.camino = camino
        self.tablero = [[self.camino for _ in range(dimension)] for _ in range(dimension)]
        self.carro = carro
        self.posicion = posicion.copy()
        self.tablero[self.posicion.x][self.posicion.y] = self.carro

    def print_board(self):
        len_tablero: int = len(self.tablero)

        print()
        for i in range(len_tablero):
            if i == 0:
                print('    ', end='')
                for j in range(len_tablero):
                    print(j, end=' ')
                print('\n   ', end='')
                print('__' * len_tablero,)
            print(i, end=' | ')
            for j in range(len_tablero):
                print(self.tablero[i][j], end=' ')
            print()
        print()

    def actulizar_posicion_carro(self, posicion: Posicion):
        self.tablero[self.posicion.x][self.posicion.y] = self.camino
        self.posicion = posicion.copy()
        self.tablero[self.posicion.x][self.posicion.y] = self.carro


def menu():

    opcion = 0
    while opcion not in range(1, 8):
        print()
        print('[1]. Arrancar', end=' ')
        print('[2]. Mover derecha', end=' ')
        print('[3]. Mover izquierda', end=' ')
        print('[4]. Mover abajo', end=' ')
        print('[5]. Mover arriba', end=' ')
        print('[6]. Apagar', end=' ')
        print('[7]. Salir')
        print()

        opcion = int(input('Ingrese una opción: '))
    return opcion


def main():
    tablero = Tablero(10)
    tablero.print_board()
    carro = Carro(10)

    while True:
        opcion = menu()
        match opcion:
            case 1:
                carro.arrancar()
            case 2:
                carro.conducir('derecha')
            case 3:
                carro.conducir('izquierda')
            case 4:
                carro.conducir('adelante')
            case 5:
                carro.conducir('atras')
            case 6:
                carro.apagar()
            case 7:
                print('Adiós')
                break

        tablero.actulizar_posicion_carro(carro.posicion)
        tablero.print_board()

if __name__ == '__main__':
    main()
