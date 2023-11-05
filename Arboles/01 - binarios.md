# Árboles binarios

## **Introducción**

Un árbol binario es una estructura de datos no lineal que se compone de nodos conectados por aristas. Los nodos representan entidades independientes que se pueden conectar a otras entidades similares. Las aristas representan las relaciones entre los nodos.

Los árboles binarios son una de las estructuras de datos más comunes en ciencias de la computación. Se utilizan para implementar estructuras de datos más complejas como conjuntos, multiconjuntos, árboles de búsqueda, árboles de expresión y más.

## **Terminología**

Antes de profundizar en los árboles binarios, es importante comprender algunos términos clave:

- **Nodo**: un nodo es un elemento individual en un árbol. Cada nodo contiene un valor y puede o no tener nodos secundarios.
- **Raíz**: la raíz es el nodo superior en un árbol. La raíz no tiene nodos padres.
- **Hijo**: un nodo hijo es un nodo que está conectado a otro nodo. El nodo conectado es el nodo padre.
- **Hoja**: una hoja es un nodo que no tiene nodos hijos.
- **Subárbol**: un subárbol es un árbol que forma parte de un árbol más grande. El subárbol puede ser un árbol completo por sí mismo.
- **Nivel**: el nivel de un nodo es la distancia entre ese nodo y la raíz. La raíz está en el nivel 0, sus nodos hijos están en el nivel 1, y así sucesivamente.
- **Altura**: la altura de un árbol es la distancia entre la raíz y el nodo más profundo. La altura de un árbol con un solo nodo es 0.
- **Profundidad**: la profundidad de un nodo es la distancia entre ese nodo y la raíz. La profundidad de la raíz es 0.

## **Árboles binarios**

Un árbol binario es un árbol en el que cada nodo tiene como máximo dos nodos hijos. Los nodos hijos se denominan comúnmente hijo izquierdo y hijo derecho.

Los árboles binarios se utilizan para implementar estructuras de datos como conjuntos, multiconjuntos, árboles de búsqueda, árboles de expresión y más.

### **Representación**

Los árboles binarios se pueden representar utilizando nodos y enlaces. Cada nodo contiene un valor y tiene dos enlaces, uno al nodo hijo izquierdo y otro al nodo hijo derecho. El nodo raíz no tiene nodos padres, por lo que sus enlaces son `None`.


### **Implementación**

Los árboles binarios se pueden implementar utilizando nodos y enlaces. Cada nodo contiene un valor y tiene dos enlaces, uno al nodo hijo izquierdo y otro al nodo hijo derecho. El nodo raíz no tiene nodos padres, por lo que sus enlaces son `None`.

```python
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
```

## **Recorrido**

Los árboles binarios se pueden recorrer utilizando un algoritmo de recorrido. Hay tres tipos de recorridos:

- **Recorrido en orden**: primero se recorre el subárbol izquierdo, luego se visita la raíz y, finalmente, se recorre el subárbol derecho.
- **Recorrido en preorden**: primero se visita la raíz, luego se recorre el subárbol izquierdo y, finalmente, se recorre el subárbol derecho.
- **Recorrido en postorden**: primero se recorre el subárbol izquierdo, luego se recorre el subárbol derecho y, finalmente, se visita la raíz.

### **Recorrido en orden**

El recorrido en orden es un algoritmo de recorrido que recorre el subárbol izquierdo, luego visita la raíz y, finalmente, recorre el subárbol derecho. El recorrido en orden se puede implementar utilizando recursión.

```python
def recorrido_en_orden(raiz):
    if raiz:
        recorrido_en_orden(raiz.izquierda)
        print(raiz.valor)
        recorrido_en_orden(raiz.derecha)
```
