# Simulador de Carron con Programación Orientada a Objetos (POO)

Este proyecto ofrece una simulación interactiva de un carro en un tablero bidimensional utilizando Python y los principios de la Programación Orientada a Objetos (POO). Consiste en dos archivos de código fuente que definen las clases necesarias y un archivo principal para ejecutar la simulación.

## Archivos de Código Fuente
- **`carro.py` :**
    Este archivo contiene la implementación de las siguientes clases:

    ***`Posicion`***: Representa una posición en un plano cartesiano. Esta clase proporciona métodos para:

    - Inicializar una posición con coordenadas `x` y `y`.
    - Mover la posición en un plano dado un desplazamiento en las coordenadas `x` y `y`.
    - Calcular la distancia entre dos posiciones.
    - Obtener las coordenadas x y y de la posición.
    - Representar la posición como una cadena de texto.

    ***`Carro`***: Representa un carro en la simulación. Esta clase tiene las siguientes características:

    - Un nivel de gasolina que se puede agotar con el tiempo.
    - Una posición actual en el tablero representada por una instancia de Posicion.
    - Métodos para arrancar, conducir en diferentes direcciones, apagar el carro y obtener la posición actual.

- **`main.py` :**
    El archivo principal de la simulación. Contiene la implementación de la clase Tablero, que representa el tablero bidimensional en el que se mueve el carro, así como una función de menú para la interacción con el usuario.

## Ejecución del Programa
Para ejecutar la simulación del carro, sigue estos pasos:

### Requisitos Previos

- Asegúrate de tener Python instalado en tu sistema.
- Descarga los archivos `carro.py` y `main.py` en un mismo directorio.

### Ejecución

Abre una terminal o línea de comandos en el directorio donde se encuentran los archivos.

Ejecuta el siguiente comando para iniciar la simulación:

```bash
python main.py
```

#### Interacción con el Carro

- Se mostrará un tablero bidimensional en la terminal junto con un menú de opciones.
- Utiliza las opciones del menú para interactuar con el carro:
    - **`Arrancar`**: Inicia el carro.
    - **`Mover derecha`**: Desplaza el carro hacia la derecha en el tablero.
    - **`Mover izquierda:`** Desplaza el carro hacia la izquierda en el tablero.
    - **`Mover abajo`**: Desplaza el carro hacia abajo en el tablero.
    - **`Mover arriba`**: Desplaza el carro hacia arriba en el tablero.
    - **`Apagar`**: Detiene el carro.
    - **`Salir`**: Finaliza la simulación.

#### Visualización en Tiempo Real

Después de cada acción seleccionada, la posición del carro se actualizará en el tablero y se mostrará en la terminal.

#### Finalización

La simulación continuará hasta que el usuario decida salir seleccionando la opción correspondiente en el menú.

## Consideraciones Adicionales
- La simulación proporciona una experiencia interactiva que permite al usuario controlar las acciones del carro en un entorno virtual.
- Los métodos y clases están diseñados siguiendo los principios de la Programación Orientada a Objetos, lo que facilita la comprensión y el mantenimiento del código.
- El diseño modular permite una fácil extensión y modificación del comportamiento del carro y del tablero en futuras iteraciones del proyecto.
