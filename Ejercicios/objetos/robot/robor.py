import posicion


class Robot:
    # figura = '🤖'
    # posicion = posicion.Posicion(0, 0)

    def __init__(self, figura='🤖', pos=posicion.Posicion(0, 0)):
        self.figura = figura
        self.posicion = pos

    def mover_derecha(self, n):
        self.posicion.aumentar_columna(n)

    def mover_arriba(self, n):
        self.posicion.aumentar_fila(-n)

    def mover_izquierda(self, n):
        self.posicion.aumentar_columna(-n)

    def mover_abajo(self, n):
        self.posicion.aumentar_fila(n)

    def mover(self, n, direccion):
        for _ in range(n):
            if direccion == 'AR':
                self.mover_arriba(1)
            elif direccion == 'AB':
                self.mover_abajo(1)
            elif direccion == 'IZ':
                self.mover_izquierda(1)
            else:
                self.mover_derecha(1)
            self.print()

    def print(self):
        print(f'{self.figura} | posicion: {self.posicion}')


robot = Robot('R', posicion.Posicion(5, 5))
robot.print()
robot.mover(3, 'AB')

robot = Robot()
robot.print()
robot.mover(3, 'AB')

robot = Robot('󰚩')
robot.print()
robot.mover(3, 'AB')

robot = Robot(pos=posicion.Posicion(5, 5))
robot.print()
robot.mover(3, 'AB')
