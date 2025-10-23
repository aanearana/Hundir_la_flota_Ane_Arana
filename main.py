import numpy as np
#Importar funciones
from utils import tablero
from utils import colocar_barcos_aleatorios
from utils import disparar

#Turnos
def turnos():
    while contador < total_turnos:
        player_1 = input("Nombre del Player 01: ")
        player_2 = input("Nombre del Player 02: ")
        turno_actual = random.choice([player_1, player_2])
        contador = 0
        total_turnos = 10
        #Imprimo aqui de quien es el turno porque si no se me imprime 10 veces
        print(f"Turno de {turno_actual}")

        # Cambiar de turno
        if turno_actual == player_1:
            turno_actual = player_1
        else:
            turno_actual = player_2
            
        contador += 1


    
    numero_barcos = input("¿Cuantos barcos deseas pintar?")
    numero_barcos = int(numero_barcos)

    eslora = input("¿Cuantas casillas ocupa el barco que deseas pintar?")
    eslora = int(eslora)

    t_barcos = colocar_barcos_aleatorios(t, numero_barcos, eslora)
    print(t_barcos)

    disparar()



#CABE NO CABE
#TURNOS con while == True hasta que uno haya pisado todos los varcos == FALSE se acaba


