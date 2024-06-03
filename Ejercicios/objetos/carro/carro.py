class Posicion:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def mover(self, delta_y, delta_x):
            self.x += delta_x
            self.y += delta_y

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y

        def distancia(self, otra_posicion):
            delta_x = self.x - otra_posicion.x
            delta_y = self.y - otra_posicion.y
            return (delta_x**2 + delta_y**2)**0.5

        def __str__(self):
            return f'Posición ({self.x}, {self.y})'

        def copy(self):
            return Posicion(self.x, self.y)


class Carro:

    def __init__(self, gasolina):
        self.gasolina = gasolina
        self.posicion = Posicion(0, 0)
        self.prendido = False

    def arrancar(self):
        if self.prendido:
            print('Ya está prendido')
        else:
            self.prendido = True
            if self.gasolina > 0:
                print('Arranca')
            else:
                print('No arranca')

    def conducir(self, direccion):
        if self.gasolina > 0 and self.prendido:
            self.gasolina -= 1

            print('Conduce hacia {direccion}')
            match direccion.lower():
                case 'adelante':
                    self.posicion.mover(0, 1)
                case 'atras':
                    self.posicion.mover(0, -1)
                case 'derecha':
                    self.posicion.mover(1, 0)
                case 'izquierda':
                    self.posicion.mover(-1, 0)
                case _:
                    print('Dirección no válida')
            print('Quedan {self.gasolina} litros')

        else:
            print('No se mueve')

    def apagar(self):
        self.prendido = False
        print('Apagado')

    def get_posicion(self):
        return self.posicion

    def __str__(self):
        return 'Carro en {self.posicion}'

