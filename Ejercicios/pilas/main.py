import register
import pila
import os


espacio = ' ' * 30


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')


def input_menu():
    opt = input(f'{espacio}    Opción: ')
    if not opt in '12345':
        return input_menu()
    return opt


def menu():
    clear()
    print(f'{espacio}⮫                     ⮪')
    print(f'{espacio}     MENU PRINCIPAL    ')
    print(f'{espacio}⮩                     ⮨')
    print()
    print(f'{espacio}1. Ingresar registro')
    print(f'{espacio}2. Mostrar registros')
    print(f'{espacio}3. Eliminar registro')
    print(f'{espacio}4. Eliminar último registro ingresado')
    print(f'{espacio}5. Salir')
    print()
    return input_menu()


def ingresar_registro():
    clear()
    print(f'{espacio}⮫                     ⮪')
    print(f'{espacio}   INGRESAR REGISTRO   ')
    print(f'{espacio}⮩                     ⮨')
    print()
    id_libro = input(f'{espacio}    ID: ')
    nombre_libro = input(f'{espacio}    Nombre: ')
    autor_libro = input(f'{espacio}    Autor: ')
    genero_libro = input(f'{espacio}    Genero: ')

    register.agregar_libro(id_libro, nombre_libro, autor_libro, genero_libro)
    pila.push(id_libro)

    print(f'{espacio}    Registro guardado')
    input(f'{espacio}    Presione enter para continuar...')


def mostrar_registros():
    clear()
    print(f'{espacio}⮫                     ⮪')
    print(f'{espacio}   MOSTRAR REGISTROS   ')
    print(f'{espacio}⮩                     ⮨')
    print()
    for libro in register.get_libros():
        print(f'{espacio}    ID: {libro[0]}')
        print(f'{espacio}    Nombre: {libro[1]}')
        print(f'{espacio}    Autor: {libro[2]}')
        print(f'{espacio}    Genero: {libro[3]}')
        print()

    input('Presione enter para continuar...')


def eliminar_registro():
    clear()
    print(f'{espacio}⮫                     ⮪')
    print(f'{espacio}   ELIMINAR REGISTRO   ')
    print(f'{espacio}⮩                     ⮨')
    print()
    id_libro = input(f'{espacio}   ID: ')
    register.borrar_libro(id_libro)

    print(f'{espacio}    Registro eliminado')
    input(f'{espacio}    Presione enter para continuar...')


def eliminar_ultimo_registro():
    clear()
    print(f'{espacio}⮫                     ⮪')
    print(f'{espacio}   ELIMINAR REGISTRO   ')
    print(f'{espacio}⮩                     ⮨')
    print()
    id_libro = pila.pop()
    if id_libro:
        register.borrar_libro(id_libro)
        print(f'{espacio}    Registro eliminado {id_libro}')
    else:
        print(f'{espacio}    No hay registros para eliminar')
    input(f'{espacio}    Presione enter para continuar...')


def main():
    while True:
        clear()
        opt = menu()
        if opt == '1':
            ingresar_registro()
        elif opt == '2':
            mostrar_registros()
        elif opt == '3':
            eliminar_registro()
        elif opt == '4':
            eliminar_ultimo_registro()
        elif opt == '5':
            break
        else:
            print(f'{espacio}    Opción inválida')
            input(f'{espacio}    Presione enter para continuar...')


if __name__ == '__main__':
    main()

