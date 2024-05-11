pila = []


def push(libro):
    pila.append(libro) # id, nombre, autor, genero


def pop():
    if not pila:
        return None
    return pila.pop()

