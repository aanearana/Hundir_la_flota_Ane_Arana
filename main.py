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

#Para iniciar el juego
juego_activo = True

#Bucle para los turnos.
while juego_activo:
    #Como el turno es aleatorio, comienza nombrando al primer jugador (Player 01 o Player 02)
    print(f"\nTurno de {turno_actual}")
    
    #Si comienza el Player 01 dispara y ve el tablero del Player 02 (oponente)
    if turno_actual == player_1:
        oponente = tablero_2
    #Si es el turno Player 02 el tablero que dispara y el que muestra es el de Player 01
    else:
        oponente = tablero_1
    
    # Mostrar un tablero oculto (solo agua y disparos, sin barcos)
    tablero_visible = np.where(oponente == "🚢", "🌊", oponente)
    #Para quitarle a las filas las comillas simples y los corchetes
    for fila in tablero_visible:
        print( " ".join(fila))


    #Para ver el tablero con los barcos
    #________________________
    #print(f"\n, Tablero Player 01 \n,{tablero_1},\n, Tablero Player 02 \n, {tablero_2} ")
    #________________________


    #Pedir coordenadas del disparo al jugador
    fila = int(input("¿A que fila del 0 al 9 quieres disparar?"))
    columna = int(input("¿A que columna del 0 al 9 quieres disparar? "))
    
    #Disparar al tablero para eso cogemos de referencia la variable en la que oponente es == a: "🚢", "🌊", oponente
    oponente = disparar(oponente, fila, columna)
    
    #Comprobar si quedan barcos, cuando no queden barcos en el tablero del oponente se muestra el jugador que ha ganado
    if "🚢" not in oponente:
        print(f"\n¡{turno_actual} ha ganado!")
        juego_activo = False
    else:
        # Cambiamos de jugador para el siguiente turno
        if turno_actual == player_1:
            turno_actual = player_2
        else:
            turno_actual = player_1

