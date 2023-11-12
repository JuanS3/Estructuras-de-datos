import json
import os


def lista_idiomas_disponibles(path: str = 'traducciones/') -> list:
    """
    Función que devuelve una lista con los idiomas disponibles.

    Parameters
    ----------
    path : str
        Ruta donde se encuentran los archivos de traducción.

    Returns
    -------
    list
        Lista con los idiomas disponibles.
    """
    path: str = os.path.join(os.getcwd(), path)
    idiomas: list[str] = [idioma[:-5] for idioma in os.listdir(path) if idioma.endswith('.json')]
    return idiomas


def cargar_idioma(idioma: str, path: str = 'traducciones/') -> dict:
    """
    Función que carga el idioma de la aplicación.

    Parameters
    ----------
    idioma : str
        Idioma a cargar.
    path : str
        Ruta donde se encuentran los archivos de traducción.

    Returns
    -------
    dict
        Diccionario con el idioma cargado.
    """
    path: str = os.path.join(os.getcwd(), path)
    with open(os.path.join(path, f'{idioma}.json'), 'r') as archivo:
        return json.load(archivo)


def clear_screen() -> None:
    """
    Función que limpia la pantalla.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main_menu(menu: dict) -> str:
    """
    Función que muestra el menú principal.

    Parameters
    ----------
    menu : dict
        Diccionario con el menú a mostrar.

    Returns
    -------
    str
        Opción elegida.
    """
    while True:
        print('===========================================')
        print(f'{menu["title"]}')
        print('===========================================')
        print()
        for key, value in menu['options'].items():
            print(f'[{key}] {value}')
        print()
        print('===========================================')
        print()
        opt = input(menu["enter_option"])
        if opt in menu['options'].keys():
            break
        else:
            clear_screen()
            print(menu['invalid_option'])
    return opt


def game() -> None:
    """
    Función que muestra el juego.
    """
    print()
    print('888888888888888888888888888888888888888888888888888888888888')
    print('888888888888888888888888888888888888888888888888888888888888')
    print('8888888888888888888888888P""  ""9888888888888888888888888888')
    print('8888888888888888P"88888P          988888"9888888888888888888')
    print('8888888888888888  "9888            888P"  888888888888888888')
    print('888888888888888888bo "9  d8o  o8b  P" od88888888888888888888')
    print('888888888888888888888bob 98"  "8P dod88888888888888888888888')
    print('888888888888888888888888    db    88888888888888888888888888')
    print('88888888888888888888888888      8888888888888888888888888888')
    print('88888888888888888888888P"9bo  odP"98888888888888888888888888')
    print('88888888888888888888P" od88888888bo "98888888888888888888888')
    print('888888888888888888   d88888888888888b   88888888888888888888')
    print('8888888888888888888oo8888888888888888oo888888888888888888888')
    print('888888888888888888888888888888888888888888888888888888888888')
    print()
    input()


def change_language(menu) -> None:
    """
    Función que cambia el idioma de la aplicación.
    """
    lista_idiomas: list[str] = lista_idiomas_disponibles()
    clear_screen()
    while True:
        print('===========================================')
        print(menu['title'])
        print('===========================================')
        print()
        for index, idioma in enumerate(lista_idiomas, start=1):
            selected: str = ' [selected]' if idioma == get_idioma() else ''
            print(f'[{index}] {idioma}{selected}')
        print()
        print('===========================================')
        print()

        opcion: int = int(input(menu["enter_option"]))
        if opcion < 1 or opcion > len(lista_idiomas):
            clear_screen()
            print(menu['invalid_option'])
        else:
            set_idioma(lista_idiomas[opcion - 1])
            break
    print(menu['change_lang'])


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


def main() -> None:
    """
    Función principal.
    """
    lista_idiomas: list[str] = lista_idiomas_disponibles()
    set_idioma(lista_idiomas[0])
    menu: dict = cargar_idioma(get_idioma())

    while True:
        clear_screen()
        opt: str = main_menu(menu['menu'])
        match opt:
            case '1':
                game()
                print(menu['menu']['thanks'])
            case '2':
                change_language(menu['change_lang'])
                menu: dict = cargar_idioma(get_idioma())
            case '3':
                break
            case _:
                print(menu['menu']['invalid_option'])
                input()


if __name__ == '__main__':
    main()
