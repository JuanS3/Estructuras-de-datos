# Pila

Una pila es una estructura de datos lineal que sigue el principio de LIFO (Last In, First Out). En una pila, los elementos se agregan y eliminan solo desde el extremo superior, también conocido como "tope" de la pila.

## Operaciones Básicas

Las operaciones básicas en una pila son las siguientes:

- **Push (Agregar)**: Agrega un elemento al tope de la pila. Este proceso se conoce como "empujar" un elemento a la pila.
- **Pop (Eliminar)**: Elimina y devuelve el elemento superior de la pila. Si la pila está vacía, esta operación resultará en un error.
- **Peek (Top)**: Devuelve el elemento superior de la pila sin eliminarlo. Esto permite ver el elemento que se retirará en la próxima operación Pop.
- **isEmpty**: Verifica si la pila está vacía. Retorna verdadero si la pila no contiene elementos, y falso de lo contrario.
- **size (Tamaño)**: Devuelve la cantidad de elementos en la pila.

## Implementaciones Comunes

Existen varias formas de implementar una pila:

- **Implementación con Arreglo (Array)**: Utiliza un arreglo para almacenar los elementos de la pila. En este enfoque, el tope de la pila se representa por el último índice del arreglo. Este método es eficiente en términos de acceso aleatorio y puede ser útil cuando se conoce el tamaño máximo de la pila.
- **Implementación con Lista Enlazada (Linked List)**: Utiliza una lista enlazada para representar la pila. En esta implementación, el último nodo de la lista enlazada es el tope de la pila. Aunque esta implementación es más flexible en términos de tamaño y puede manejar pilas de tamaño variable, puede tener un mayor costo de espacio debido a los punteros adicionales en cada nodo.

## Comportamiento y Complejidad

El comportamiento y la complejidad de las operaciones comunes en una pila son los siguientes:

- **Push**: \(O(1)\) - La inserción en una pila es una operación constante, ya que simplemente se agrega un elemento en el tope de la pila.
- **Pop**: \(O(1)\) - La eliminación en una pila también es una operación constante, ya que solo se elimina el elemento superior de la pila.
- **Peek**: \(O(1)\) - Obtener el elemento superior de la pila sin eliminarlo también es una operación constante.
- **isEmpty**: \(O(1)\) - Verificar si la pila está vacía es una operación constante, ya que solo se comprueba si la lista subyacente está vacía.
- **size**: \(O(1)\) - Devolver la cantidad de elementos en la pila es una operación constante ya que el tamaño se almacena como una variable.

## Uso y Aplicaciones

Las pilas se utilizan en una variedad de aplicaciones, incluyendo:

- **Manejo de Memoria**: Las pilas se utilizan en la administración de memoria durante la ejecución de programas, especialmente en la gestión de la pila de llamadas (call stack) en la ejecución de funciones.
- **Evaluación de Expresiones**: Las pilas se utilizan en la evaluación de expresiones matemáticas, especialmente en la notación polaca inversa (postfix), donde las operaciones se realizan de manera eficiente utilizando una pila.
- **Seguimiento de Ejecución**: Las pilas se utilizan en la depuración de programas para rastrear la secuencia de llamadas de función (stack trace) y la secuencia de ejecución del código.

## Ejemplos de Uso en la Vida Diaria

Además de las aplicaciones mencionadas, las pilas se utilizan en la vida diaria de las siguientes formas:

- **Historial de Navegación en un Navegador Web**: Los navegadores web utilizan una pila para mantener un historial de las páginas web visitadas.
- **Undo/Redo en Editores de Texto o Software de Edición de Imágenes**: Funciones como "Deshacer" (Undo) y "Rehacer" (Redo) en programas de edición de texto o imágenes utilizan pilas para almacenar el historial de acciones realizadas por el usuario.

