class Posicion:

    def __init__(self, x, y):
        self.fila = x
        self.columna = y

    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna

    def aumentar_fila(self, n):
        self.fila += n # self.fila = self.fila + n

    def aumentar_columna(self, n):
        self.columna += n

    def print(self, nombre):
        print(f'Posicion {nombre}: {self.fila}, {self.columna}')

    def __str__(self):
        return f'X -> {self.fila}, Y -> {self.columna}'
