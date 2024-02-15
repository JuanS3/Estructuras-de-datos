# Recursividad en Python

La recursión es un concepto en programación en el cual una función se llama a sí misma para resolver un problema. Es similar a una estructura de bucle, pero en lugar de repetir un bloque de código, la función se divide en tareas más pequeñas y se resuelve a través de llamadas recursivas.

La recursión es especialmente útil para abordar problemas que pueden descomponerse en subproblemas más simples y similares. A menudo, se utiliza en algoritmos que siguen la idea de "divide y vencerás".

## Elementos de la recursión

La recursión se compone de dos elementos principales:

- **Caso base**: es el caso más simple de un problema que se puede resolver directamente. El caso base se utiliza para detener la recursión cuando el problema se ha resuelto.

- **Caso recursivo**: es el caso en el que el problema se divide en subproblemas más pequeños. El caso recursivo utiliza la recursión para resolver los subproblemas.

## Ejemplo de recursión

El siguiente ejemplo muestra una función que calcula el factorial de un número:

Un ejemplo clásico de uso de la recursión es el cálculo del factorial de un número. El factorial de un número entero positivo `n` se define como el producto de todos los números enteros positivos desde 1 hasta `n`.

Por ejemplo, el factorial de 5 se calcula como:

```python
5! = 5 * 4!
   = 5 * 4 * 3!
   = 5 * 4 * 3 * 2!
   = 5 * 4 * 3 * 2 * 1!
   = 5 * 4 * 3 * 2 * 1 * 0!
   = 5 * 4 * 3 * 2 * 1 * 1
   = 5 * 4 * 3 * 2 * 1
   = 5 * 4 * 3 * 2
   = 5 * 4 * 6
   = 5 * 24
   = 120
```

La función factorial se puede definir de la siguiente manera:

```python
def factorial(n):
    # Caso base
    if n == 0:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)
```

En este ejemplo, el caso base es cuando `n` es `0` o `1`, en cuyo caso el factorial es `1`. En el caso recursivo, la función se llama a sí misma con `n - 1` y se multiplica por `n`. Esto continúa hasta que `n` es `0` o `1`, momento en el que la función comienza a regresar resultados.

---
### Recursos

- [Recursividad en Python / Jupyter Notebook](02%20-%20Recursividad.ipynb)
---

<div style="text-align: center">

[🔙 Arreglos](01%20-%20arreglos.md) | [🔼 Subir](#recursividad) | [🔜 Listas enlazadas](03%20-%20listas%20enlazadas.md)

</div>

