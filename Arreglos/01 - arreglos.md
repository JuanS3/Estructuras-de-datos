# Arreglos

Un arreglo es una estructura de datos que contiene una colección de elementos del mismo tipo. Los arreglos se utilizan para almacenar datos de manera eficiente y compacta. Por ejemplo, si desea almacenar 100 números enteros, es mucho más fácil hacerlo en un arreglo que en 100 variables separadas.

En Python se pueden crear arreglos basados en listas y tuplas, la diferencia principal entre esos es que las listas son mutables y las tuplas son inmutables

Las listas son una de las estructuras de datos más importantes en Python. Se utilizan para almacenar una colección ordenada de datos de cualquier tipo. Pueden contener enteros, cadenas, flotantes, objetos, o incluso otras listas, esto se debe a como están implementados los tipos de datos en Python, puesto que todos son Objetos, lo que permite que el lenguaje presente una versatilidad alta.

## Creación de arreglos

### Desde una lista

Para crear un arreglo desde una lista puede hacer de dos formas, la primera es usando la función `list()` y la segunda es usando la notación de corchetes `[]`. A continuación se muestran ejemplos de ambas formas:

```python
# Creación de un arreglo desde una lista usando la función list()
arreglo = list([1, 2, 3, 4, 5])
print(arreglo)
```

```python
# Creación de un arreglo desde una lista usando la notación de corchetes []
arreglo = [1, 2, 3, 4, 5]
print(arreglo)
```

### Desde una tupla

Para crear un arreglo desde una tupla puede hacer de dos formas, la primera es usando la función `tuple()` y la segunda es usando la notación de paréntesis `()`. A continuación se muestran ejemplos de ambas formas:

```python
# Creación de un arreglo desde una tupla usando la función tuple()
arreglo = tuple((1, 2, 3, 4, 5))
print(arreglo)
```

```python
# Creación de un arreglo desde una tupla usando la notación de paréntesis ()
arreglo = (1, 2, 3, 4, 5)
print(arreglo)
```

## Listas VS Tuplas

Las listas y las tuplas son muy similares, pero tienen algunas diferencias clave. La principal diferencia entre las listas y las tuplas es que las listas son mutables, mientras que las tuplas son inmutables. Esto significa que las listas se pueden modificar, pero las tuplas no.

### Listas

Las listas son mutables, lo que significa que se pueden modificar después de su creación. Puede agregar elementos, eliminar elementos, cambiar el orden de los elementos, etc.

### Tuplas

Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación. Esto significa que no puede agregar, eliminar o cambiar elementos de la tupla.

## Recorrido de arreglos

En python ***no existe el for tradicional*** (`for(i=0; i < n; i++){...}`) sino que se implementa el ***for each*** que es una variación que facilita el recorrido de elementos en estructuras de datos como listas, tuplas, diccionarios y más. El bucle **for each** itera automáticamente sobre cada elemento en la estructura, eliminando la necesidad de gestionar manualmente el índice o el contador, como se hace en el **for** tradicional.

La sintaxis básica del bucle **for each** en Python es la siguiente:

```python
for elemento in estructura_de_datos:
    # Hacer algo con el elemento
```

Aquí, **elemento** es una variable que tomará el valor de cada elemento en la **estructura_de_datos** en cada iteración del bucle. Por ejemplo, si deseas recorrer una lista de números y mostrar cada número, puedes hacerlo de la siguiente manera:

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

Este código imprimirá los números del 1 al 5, uno en cada línea. El bucle **for each** también puede utilizarse con otras *estructuras de datos*, como diccionarios, donde el **elemento** representará las claves en cada iteración, permitiéndote acceder a los valores correspondientes.

En resumen, el bucle **for each** en Python ofrece una manera más simple y legible de recorrer elementos en estructuras de datos, sin preocuparse por el control manual de los índices. Esto hace que el código sea más limpio y menos propenso a errores.

## Operaciones con arreglos

### Acceso a elementos

Para acceder a un elemento de un arreglo se usa la notación de corchetes `[]` y dentro de los corchetes se coloca el índice del elemento que se desea acceder. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
print(arreglo[0])
```

### Modificación de elementos

Para modificar un elemento de un arreglo se usa la notación de corchetes `[]` y dentro de los corchetes se coloca el índice del elemento que se desea modificar. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
arreglo[0] = 10
print(arreglo)
```

### Eliminación de elementos

Para eliminar un elemento de un arreglo se usa la función `del` y dentro de los paréntesis se coloca el arreglo y el índice del elemento que se desea eliminar. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
del arreglo[0]
print(arreglo)
```

### Agregar elementos

Para agregar un elemento a un arreglo se usa la función `append()` y dentro de los paréntesis se coloca el elemento que se desea agregar. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
arreglo.append(6)
print(arreglo)
```

### Longitud de un arreglo

Para obtener la longitud de un arreglo se usa la función `len()` y dentro de los paréntesis se coloca el arreglo. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
print(len(arreglo))
```

### Ordenar un arreglo

Para ordenar un arreglo se usa la función `sort()` y dentro de los paréntesis se coloca el arreglo. A continuación se muestra un ejemplo:

```python
arreglo = [5, 4, 3, 2, 1]
arreglo.sort()
print(arreglo)
```

### Invertir un arreglo

Para invertir un arreglo se usa la función `reverse()` y dentro de los paréntesis se coloca el arreglo. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
arreglo.reverse()
print(arreglo)
```

### Copiar un arreglo

Para copiar un arreglo se usa la función `copy()` y dentro de los paréntesis se coloca el arreglo. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
copia = arreglo.copy()
print(copia)
```

### Contar elementos

Para contar un elemento en un arreglo se usa la función `count()` y dentro de los paréntesis se coloca el arreglo y el elemento que se desea contar. A continuación se muestra un ejemplo:

```python
arreglo = [1, 2, 3, 4, 5]
print(arreglo.count(1))
```

### Otras operaciones

Existen muchas otras operaciones que se pueden realizar con arreglos, para conocerlas todas se recomienda revisar la documentación oficial de Python en el siguiente enlace: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)