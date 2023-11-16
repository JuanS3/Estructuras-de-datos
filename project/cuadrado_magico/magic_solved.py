from consoleverse import console


def init_square(n: int) -> list[list[int]]:
    """
    Función que inicializa un cuadrado de orden n.

    Parameters
    ----------
    n : int
        Orden del cuadrado.

    Returns
    -------
    list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    cuadrado = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    return cuadrado


def print_square(square: list[list[int]]) -> None:
    """
    Función que imprime un cuadrado.

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    console.println('Cuadrado Mágico:', style='bold', color='green')
    console.new_line()
    console.print_matrix(square, color_index='yellow', color='blue', color_style='cyan')


def is_valid_square(square: list[list[int]]) -> bool:
    """
    Función que verifica si un cuadrado es válido.
    El cuadrado es válido si todos los números son distintos y están en el rango [1, n^2].

    Examples
    --------
    >>> is_valid_square([[1, 2], [3, 4]])
    True
    >>> is_valid_square([[1, 2], [3, 1]])
    False

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.

    Returns
    -------
    bool
        True si el cuadrado es válido, False en caso contrario.
    """
    for row in square:
        for value in row:
            if value < 1 or value > len(square) ** 2:
                console.println(
                    f'El valor {value} es inválido, debe estar en el rango [1, {len(square) ** 2}]',
                    color='yellow',
                    style='bold'
                )
                return False
    return True


def is_magic_square(square: list[list[int]]) -> bool:
    """
    Función que verifica si un cuadrado es mágico.
    El cuadrado es mágico si es válido y la suma de cada fila, columna y diagonal es la misma.

    Examples
    --------
    >>> is_magic_square([[1, 2], [3, 4]])
    False

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.

    Returns
    -------
    bool
        True si el cuadrado es mágico, False en caso contrario.
    """
    if not is_valid_square(square):
        return False
    n = len(square)
    magic_sum = sum(square[0])
    for row in square:
        if sum(row) != magic_sum:
            console.println(
                f'La fila {row} no es mágica {sum(row)} | {magic_sum}',
                color='yellow',
                style='bold'
            )
            return False
    for col in range(n):
        if sum(row[col] for row in square) != magic_sum:
            console.println(
                f'La columna {col} no es mágica {sum(row[col] for row in square)} | {magic_sum}',
                color='yellow',
                style='bold'
            )
            return False
    if sum(square[i][i] for i in range(n)) != magic_sum:
        console.println(
            f'La diagonal principal no es mágica {sum(square[i][i] for i in range(n))} | {magic_sum}',
            color='yellow',
            style='bold'
        )
        return False
    if sum(square[i][n - i - 1] for i in range(n)) != magic_sum:
        console.println(
            f'La diagonal secundaria no es mágica {sum(square[i][n - i - 1] for i in range(n))} | {magic_sum}',
            color='yellow',
            style='bold'
        )
        return False
    return True


def set_value(square: list[list[int]], col: int, row: int, value: int) -> None:
    """
    Función que asigna un valor a una posición del cuadrado.

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.
    col : int
        Columna.
    row : int
        Fila.
    value : int
        Valor a asignar.
    """
    if col < 0 or col >= len(square):
        console.println(
            f'La columna {col} es inválida, debe estar en el rango [0, {len(square) - 1}]',
            color='red',
            style='bold'
        )
        return
    if row < 0 or row >= len(square):
        console.println(
            f'La fila {row} es inválida, debe estar en el rango [0, {len(square) - 1}]',
            color='red',
            style='bold'
        )
        return
    if value < 1 or value > len(square) ** 2:
        console.println(
            f'El valor {value} es inválido, debe estar en el rango [1, {len(square) ** 2}]',
            color='red',
            style='bold'
        )
        return
    square[row][col] = value


def menu() -> int:
    """
    Función que muestra el menú y retorna la opción seleccionada.

    Returns
    -------
    int
        Opción seleccionada.
    """
    console.clear_screen()
    console.new_line()
    console.println('Menú', style='bold', color='blue')
    console.new_line()

    console.println('1.', style='bold', color='blue', endl=' ')
    console.println('Ingresar un valor')

    console.println('2.', style='bold', color='blue', endl=' ')
    console.println('Verificar si es mágico')

    console.println('3.', style='bold', color='blue', endl=' ')
    console.println('Mostrar cuadrado')

    console.println('4.', style='bold', color='blue', endl=' ')
    console.println('Salir')

    console.new_line()
    option = int(console.inputln('Ingrese una opción: ', style='bold'))
    return option


def init_game() -> list[list[int]]:
    """
    Función que inicializa el juego.

    Returns
    -------
    list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    console.clear_screen()
    console.new_line()
    console.println('Cuadrado mágico', style='bold', color='blue')
    console.new_line()
    n = int(console.inputln('Ingrese el orden del cuadrado mágico: '))
    console.new_line()
    console.println('El cuadrado mágico de orden', n, 'es:')
    console.new_line()
    cuadrado_magico = init_square(n)
    print_square(cuadrado_magico)
    console.inputln('\nPresione enter para continuar', style='bold')
    return cuadrado_magico


def main():
    cuadrado_magico = init_game()
    while True:
        match menu():
            case 1:
                console.clear_screen()
                console.new_line()
                console.println('Ingresar un valor', style='bold', color='blue')
                console.new_line()
                row = int(console.inputln('Ingrese la fila: ', style='bold'))
                col = int(console.inputln('Ingrese la columna: ', style='bold'))
                value = int(console.inputln('Ingrese el valor: ', style='bold'))
                set_value(cuadrado_magico, col, row, value)
                console.inputln('\nPresione enter para continuar', style='bold')
            case 2:
                console.clear_screen()
                console.new_line()
                console.println('Verificar si es mágico', style='bold', color='blue')
                console.new_line()
                if is_magic_square(cuadrado_magico):
                    console.println('El cuadrado es mágico', style='bold', color='green')
                else:
                    console.println('El cuadrado no es mágico', style='bold', color='red')
                console.inputln('\nPresione enter para continuar', style='bold')
            case 3:
                console.clear_screen()
                console.new_line()
                console.println('Mostrar cuadrado', style='bold', color='blue')
                console.new_line()
                print_square(cuadrado_magico)
                console.inputln('\nPresione enter para continuar', style='bold')
            case 4:
                console.clear_screen()
                console.new_line()
                console.println('Salir', style='bold', color='blue')
                console.new_line()
                console.println('Gracias por jugar', style='bold', color='green')
                return
            case _:
                console.clear_screen()
                console.new_line()
                console.println('Opción inválida', style='bold', color='red')
                console.new_line()
                console.inputln('\nPresione enter para continuar', style='bold')
                continue


main()
