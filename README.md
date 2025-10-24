# Hundir la Flota en Python

Un pequeño juego de Hundir la Flota (Battleship) hecho en Python, pensado para practicar listas, bucles y funciones.

Está programado de manera simple y clara para que cualquier principiante pueda entender cómo funciona.

## Estructura del proyecto

El proyecto tiene dos archivos principales:

1. main.py → controla el flujo del juego (pedir nombres, turnos, disparos, ganador, etc.)

2. utils.py → contiene las funciones necesarias para crear el tablero, colocar los barcos y realizar los disparos.

## Cómo jugar

1. Ejecuta el archivo main.py en la terminal mendiante: python main.py

2. Responde las preguntas:

- Nombre del Player
- ¿Cuántos barcos quieres colocar? 
- ¿Qué tamaño tendrán tus barcos?
- Elige la fila a disparar (0-9)
- Columna a disparar (0-9)

3. En cada turno:

- El jugador elegirá una fila y una columna para disparar (valores del 0 al 9).

- Si acierta un barco, se marcará con 💀.

- Si falla, se marcará con 🔴.

- El juego termina cuando uno de los jugadores hunde todos los barcos del oponente.

## Símbolos del tablero
### Símbolo	Significado
🌊	Agua
🚢	Barco
🔴	Disparo fallado
💀	Barco hundido

## Requisitos

Para ejecutar el juego, necesitas tener instalado:

- Python 3

- NumPy

- Puedes instalar NumPy ejecutando:

- pip install numpy
