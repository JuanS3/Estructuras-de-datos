import os
import productos


ESPACIOS = ' ' * 10

def clear_scren():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    clear_scren()
    print()
    print(rf'{ESPACIOS}__| |____________________________________________________| |__')
    print(rf'{ESPACIOS}__   ____________________________________________________   __')
    print(rf'{ESPACIOS}  | |                                                    | |')
    print(rf'{ESPACIOS}  | |  ______  ______  __  __  ______  ______  ______    | |')
    print(rf'{ESPACIOS}  | | /\  ___\/\  == \/\ \/\ \/\__  _\/\  __ \/\  ___\   | |')
    print(rf'{ESPACIOS}  | | \ \  __\\ \  __<\ \ \_\ \/_/\ \/\ \  __ \ \___  \  | |')
    print(rf'{ESPACIOS}  | |  \ \_\   \ \_\ \_\ \_____\ \ \_\ \ \_\ \_\/\_____\ | |')
    print(rf'{ESPACIOS}  | |   \/_/    \/_/ /_/\/_____/  \/_/  \/_/\/_/\/_____/ | |')
    print(rf'{ESPACIOS}__| |____________________________________________________| |__')
    print(rf'{ESPACIOS}__   ____________________________________________________   __')
    print(rf'{ESPACIOS}  | |                                                    | |')
    print()


def menu_principal():
    title()
    print(f'{ESPACIOS}1. Agregar un nuevo producto')
    print(f'{ESPACIOS}2. Ver todos los productos')
    print(f'{ESPACIOS}3. Eliminar un producto')
    print(f'{ESPACIOS}4. Salir')


def menu_agregar():
    title()
    codigo_producto = input(f'{ESPACIOS}Ingresa el codigo del nuevo producto: ')
    productos.productos[codigo_producto] = productos.ESTRUCTURA_BASE_PRODUCTO

    for attr in productos.ESTRUCTURA_BASE_PRODUCTO:
        productos.productos[codigo_producto][attr] = input(f'{ESPACIOS}{ESPACIOS}Ingresa el valor de {attr}: ')

    print(f'{ESPACIOS}Producto agregado correctamente')
    input(f'{ESPACIOS}Presiona enter para continuar...')


def ver_productos():
    title()
    for cod in productos.productos:
        print(f'{ESPACIOS}--------------------------------------------')
        print(f'{ESPACIOS}CODIGO: ', cod)

        for attr in productos.productos[cod]:
            print(f'{ESPACIOS}{attr} : {productos.productos[cod][attr]}')

        print(f'{ESPACIOS}--------------------------------------------')

    input(f'{ESPACIOS}Presiona enter para continuar...')


def eliminar_producto():
    title()
    id = input(f'{ESPACIOS}Ingresa el ID del producto a eliminar: ')
    productos.productos.pop(id, None)
    print(f'{ESPACIOS}Producto eliminado correctamente')
    input(f'{ESPACIOS}Presiona enter para continuar...')


if __name__ == '__main__':
    while True:
        menu_principal()
        op = input(f'{ESPACIOS}Ingresa una opcion: ')
        if op == '1':
            menu_agregar()
        elif op == '2':
            ver_productos()
        elif op == '3':
            eliminar_producto()
        elif op == '4':
            break












