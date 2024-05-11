libros = [
    ('AB3cd', 'Harry Potter', 'J.K. Rowling', 'Fantasía'),
    ('PqRs7', 'Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico'),
    ('gH9t2', '1984', 'George Orwell', 'Distopía'),
    ('VxYz4', 'Orgullo y prejuicio', 'Jane Austen', 'Romance'),
    ('JKlM6', 'El nombre del viento', 'Patrick Rothfuss', 'Fantasía épica'),
    ('78RtS', 'Crónica de una muerte anunciada', 'Gabriel García Márquez', 'Ficción'),
    ('A3d8e', 'El señor de los anillos', 'J.R.R. Tolkien', 'Fantasía épica'),
    ('T9s2M', 'Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela'),
    ('zXyH7', 'Matar a un ruiseñor', 'Harper Lee', 'Ficción'),
    ('4BnM2', 'Las aventuras de Sherlock Holmes', 'Arthur Conan Doyle', 'Detective'),
]


def agregar_libro(id_libro, nombre_libro, autor_libro, genero_libro):
    libros.append(
        (id_libro, nombre_libro, autor_libro, genero_libro)
    )


def borrar_libro(id_libro):
    for libro in libros:
        if libro[0] == id_libro:
            libros.remove(libro)
            break


def buscar_libro(parametro, valor):
    lib = None

    if parametro == 'id':
        for libro in libros:
            if libro[0] == valor:
                lib = libro

    elif parametro == 'nombre':
        for libro in libros:
            if libro[1] == valor:
                lib = libro

    elif parametro == 'autor':
        for libro in libros:
            if libro[2] == valor:
                lib = libro

    elif parametro == 'genero':
        for libro in libros:
            if libro[3] == valor:
                lib = libro

    return lib


def get_libros():
    return libros

