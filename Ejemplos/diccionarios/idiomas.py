import sys
import os


_idioma = IDIOMA_DEFECTO = 'es'

_idiomas = {
    'es': {
        'menu': {
            'titulo': 'Menú',
            'opciones': {
                '1': 'Jugar',
                '2': 'Cambiar idioma',
                '3': 'Salir'
            },
            'opcion_invalida': 'Opción inválida',
            'gracias': 'Gracias por jugar',
            'ingrese_opcion': 'Ingrese una opción: '
        },
        'cambiar_idioma': {
            'titulo': 'Cambiar idioma',
            'opciones': {
                '1': 'Español',
                '2': 'Inglés'
            },
            'opcion_invalida': 'Opción inválida',
            'idioma_cambiado': 'Idioma cambiado',
            'ingrese_opcion': 'Ingrese una opción: '
        }
    },
    'en': {
        'menu': {
            'titulo': 'Menu',
            'opciones': {
                '1': 'Play',
                '2': 'Change language',
                '3': 'Exit'
            },
            'opcion_invalida': 'Invalid option',
            'gracias': 'Thanks for playing',
            'ingrese_opcion': 'Enter an option: '
        },
        'cambiar_idioma': {
            'titulo': 'Change language',
            'opciones': {
                '1': 'Spanish',
                '2': 'English'
            },
            'opcion_invalida': 'Invalid option',
            'idioma_cambiado': 'Language changed',
            'ingrese_opcion': 'Enter an option: '
        }
    }
}


def clear_screen() -> None:
    """
    Función que limpia la pantalla.
    """
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


def set_idioma(idioma: str) -> None:
    """
    Función que establece el idioma de la aplicación.

    Parameters
    ----------
    idioma : str
        Idioma a establecer.
    """
    global _idioma
    _idioma = idioma


def get_idioma() -> str:
    """
    Función que devuelve el idioma de la aplicación.

    Returns
    -------
    str
        Idioma de la aplicación.
    """
    return _idioma


def cambiar_idioma() -> None:
    """
    Función que cambia el idioma de la aplicación.
    """
    print('===========================================')
    print(f'{_idiomas[get_idioma()]["cambiar_idioma"]["titulo"]}')
    print('===========================================')
    print()
    print(f'[1] {_idiomas[get_idioma()]["cambiar_idioma"]["opciones"]["1"]}')
    print(f'[2] {_idiomas[get_idioma()]["cambiar_idioma"]["opciones"]["2"]}')
    print()
    print('===========================================')
    print()
    opcion = input(f'{_idiomas[get_idioma()]["cambiar_idioma"]["ingrese_opcion"]}')
    if opcion == '1':
        set_idioma('es')
        print(_idiomas[get_idioma()]["cambiar_idioma"]["idioma_cambiado"])
    elif opcion == '2':
        set_idioma('en')
        print(_idiomas[get_idioma()]["cambiar_idioma"]["idioma_cambiado"])
    else:
        clear_screen()
        print(_idiomas[get_idioma()]["cambiar_idioma"]["opcion_invalida"])
        cambiar_idioma()


def menu() -> str:
    """
    Menú de la aplicación.

    Returns
    -------
    str
        Opción seleccionada.
    """
    print('===========================================')
    print(f'{_idiomas[get_idioma()]["menu"]["titulo"]}')
    print('===========================================')
    print()
    print(f'[1] {_idiomas[get_idioma()]["menu"]["opciones"]["1"]}')
    print(f'[2] {_idiomas[get_idioma()]["menu"]["opciones"]["2"]}')
    print(f'[3] {_idiomas[get_idioma()]["menu"]["opciones"]["3"]}')
    print()
    print('===========================================')
    print()
    opcion = input(f'{_idiomas[get_idioma()]["menu"]["ingrese_opcion"]}')
    if opcion == '1':
        return '1'
    elif opcion == '2':
        return '2'
    elif opcion == '3':
        return '3'
    else:
        clear_screen()
        print(_idiomas[get_idioma()]["menu"]["opcion_invalida"])
        return menu()




if __name__ == '__main__':
    clear_screen()
    while True:
        opcion = menu()
        if opcion == '1':
            clear_screen()
            print('Jugar')
        elif opcion == '2':
            clear_screen()
            cambiar_idioma()
        elif opcion == '3':
            clear_screen()
            print('Chao')
            break
        else:
            print('Opción inválida')
