import numpy as np
import random
from utils import tablero, colocar_barcos_aleatorios, disparar

# Pedir nombres
player_1 = input("Nombre del Player 01: ")
player_2 = input("Nombre del Player 02: ")


# Elegir de manera aleatoria entre los dos nombres
turno_actual = random.choice([player_1, player_2])

# Crear tableros vacíos para ambos jugadores
tablero_1 = tablero()
tablero_2 = tablero()

# Colocar barcos en ambos tableros
print(f"\n{player_1}, coloca tus barcos:")
num_barcos = int(input("¿Cuántos barcos quieres colocar? "))
eslora = int(input("¿Qué tamaño tendrán tus barcos? "))
tablero_1 = colocar_barcos_aleatorios(tablero_1, num_barcos, eslora)

print(f"\n{player_2}, coloca tus barcos:")
num_barcos = int(input("¿Cuántos barcos quieres colocar? "))
eslora = int(input("¿Qué tamaño tendrán tus barcos? "))
tablero_2 = colocar_barcos_aleatorios(tablero_2, num_barcos, eslora)

# Decidir quién empieza
turno_actual = random.choice([player_1, player_2])
print(f"\nEmpieza {turno_actual}!")

# Iniciar el juego
juego_activo = True
while juego_activo:
    print(f"\nTurno de {turno_actual}")
    
    # Seleccionar tablero del oponente
    if turno_actual == player_1:
        oponente = tablero_2
    else:
        oponente = tablero_1
    
    # Mostrar un tablero oculto (solo agua y disparos, sin barcos)
    tablero_visible = np.where(oponente == "🚢", "🌊", oponente)
    print(tablero_visible)
    
    # Pedir coordenadas del disparo
    fila = int(input("Fila a disparar (0-9): "))
    columna = int(input("Columna a disparar (0-9): "))
    
    # Disparar
    oponente = disparar(oponente, fila, columna)
    
    # Comprobar si quedan barcos
    if "🚢" not in oponente:
        print(f"\n¡{turno_actual} ha ganado! 🚢💥")
        juego_activo = False
    else:
        # Cambiar de turno
        turno_actual = player_2 if turno_actual == player_1 else player_1