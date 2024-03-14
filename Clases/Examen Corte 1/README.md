# Parte Práctica: Implementación de Movimiento del Robot en la Bodega

Imagine que ha sido incorporado al equipo de desarrollo de la empresa ***FutureRobotic***, específicamente para finalizar la implementación de una función crucial para uno de sus robots de próxima generación: el Robot Acomodador de Bodega V2.

Se le ha encomendado la tarea de completar el código de una función que permita el movimiento del robot dentro de una bodega, representada como una matriz de dimensiones n x m. Esta matriz consta de los siguientes elementos:

- **`#`**: Representa un obstáculo que el robot no puede atravesar.
- **`.`**: Representa un espacio libre por el que el robot puede moverse.
- **`S`**: Indica la posición inicial del robot.
- **`E`**: Indica la posición del paquete a recoger.

La función debe permitir al robot moverse en cuatro direcciones posibles:

- **`U`**: Arriba
- **`D`**: Abajo
- **`L`**: Izquierda
- **`R`**: Derecha

Además, el usuario proporcionará un número entero `k`, que indica la cantidad de casillas que el robot debe moverse en la dirección especificada.

## Requerimientos

**La función debe cumplir con los siguientes requerimientos:**

- Si el movimiento solicitado no es posible debido a un obstáculo (**`#`**) o a los límites de la matriz, la función debe retornar **`False`** y **no realizar ningún movimiento**.

- Si el movimiento es válido, la función debe retornar **`True`** y efectuar el desplazamiento del robot en la dirección especificada, tenga el cuenta pueden existir solor 3 casillas disponibles para avanzar y que el valor de **`k`** puede ser mayor, en este caso, el movimiento será tomado como válido y el robot se moverá a la casilla limite, es decir, si tiene 3 casillas disponibles y **`k`** es igual a 5, el robot se moverá 3 casillas.

## Ejemplos:

Estado inicial

```
| 1 | - # # # # # # # # # # |
| 2 | - # S . . . . . . . # |
| 3 | - # . # . # # # # . # |
| 4 | - # . # . . . # # . # |
| 5 | - # . # # # . # # . # |
| 6 | - # . # # . . # # . # |
| 7 | - # . # # . # # # . # |
| 8 | - # . . . . . . # E # |
| 9 | - # # # # # # # # # # |
```

### Ejemplo 1:

Con **`k = 1`** y **`dirección = 'R'`**

Salida esperada:

```
| 1 | - # # # # # # # # # # |
| 2 | - # . S . . . . . . # |
| 3 | - # . # . # # # # . # |
| 4 | - # . # . . . # # . # |
| 5 | - # . # # # . # # . # |
| 6 | - # . # # . . # # . # |
| 7 | - # . # # . # # # . # |
| 8 | - # . . . . . . # E # |
| 9 | - # # # # # # # # # # |
```

### Ejemplo 2:

Con **`k = 4`** y **`dirección = 'L'`**

Salida esperada:

```
| 1 | - # # # # # # # # # # |
| 2 | - # S . . . . . . . # |
| 3 | - # . # . # # # # . # |
| 4 | - # . # . . . # # . # |
| 5 | - # . # # # . # # . # |
| 6 | - # . # # . . # # . # |
| 7 | - # . # # . # # # . # |
| 8 | - # . . . . . . # E # |
| 9 | - # # # # # # # # # # |
```

### Ejemplo 3:

Con **`k = 1`** y **`dirección = 'U'`**

Salida esperada:

```
| 1 | - # # # # # # # # # # |
| 2 | - # S . . . . . . . # |
| 3 | - # . # . # # # # . # |
| 4 | - # . # . . . # # . # |
| 5 | - # . # # # . # # . # |
| 6 | - # . # # . . # # . # |
| 7 | - # . # # . # # # . # |
| 8 | - # . . . . . . # E # |
| 9 | - # # # # # # # # # # |
```

### Ejemplo 4:

Con **`k = 20`** y **`dirección = 'D'`**

Salida esperada:

```
| 1 | - # # # # # # # # # # |
| 2 | - # . . . . . . . . # |
| 3 | - # . # . # # # # . # |
| 4 | - # . # . . . # # . # |
| 5 | - # . # # # . # # . # |
| 6 | - # . # # . . # # . # |
| 7 | - # . # # . # # # . # |
| 8 | - # S . . . . . # E # |
| 9 | - # # # # # # # # # # |
```
