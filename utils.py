#1. Diseñar el tablero
import numpy as np
import random

#Pintar el tablero
def tablero():
    "No necesita parametros, tiene predeterminado 10x10"
    tablero = np.full((10,10), "🌊")
    return tablero

#Para pintar los barcos
def colocar_barcos_aleatorios(tablero, numero_barcos, eslora):
    '''
    Parametros:
        tablero = añadir el tablero del jugador 
        numero_barcos = Cuantos barcos queremos añadir en el tablero
        eslora = como de grande queremos que sea nuestro barco
    '''
    try:
        #Para que el valor que nos de el jugador sea un valor entero
        numero_barcos = int(numero_barcos)
        eslora = int(eslora)
    #Si los valores que nos da el jugador no son compatibles con mi funcion da error (float, str...)
    except ValueError:
        return "Error!"

    #Iniciamos contando del punto 0,0
    tamaño = tablero.shape[0]

    #Iniciamos el contador de barcos a 0
    barcos_colocados = 0
    
    while barcos_colocados < numero_barcos:
        colocado = False
        intentos = 0
        
        #Cuando colocados == False y entra en la funcion y comienza a colocar aleatoriamente
        #Para que no se quede pillado, intentos <500
        while not colocado and intentos < 500: 
            #Suma uno a los intentos
            intentos += 1
            #Elige la dirección aleatorio, elige entre H(Horizontal) y V(Vertical)
            direccion = random.choice(['H', 'V'])
            
            #Si elige H(Horizontal)
            if direccion == 'H':
                #La fila puede ser aleatoriamente des de el primer elemento hasta el utlimo
                fila = random.randint(0, tamaño - 1)
                #Igual que el otro pero al ser horizontal tiene en cuenta el tamaño de la eslora para que no salga del tablero
                columna = random.randint(0, tamaño - eslora)
                #Repite la tupla de fila columna en funcion del tamaño de la eslora
                coordenadas_barco = [(fila, columna + i) for i in range(eslora)]
            
            #Si elige V(Vertical)
            else:
                #Tiene en cuenta el tamaño de la eslora para que no salga del tablero
                fila = random.randint(0, tamaño - eslora)
                #Coge los valores desde el primer elemento hasta el utlimo
                columna = random.randint(0, tamaño - 1)
                #Si la direcion a salido H, añade a la lista de barcos una tupla
                coordenadas_barco = [(fila + i, columna) for i in range(eslora)]
            
            casillas_libres = True 

            for x, y in coordenadas_barco:
            #Si la casilla ya esta ocpupada, es decir ya hay un barco
                if tablero[x, y] == "🚢":  
                    casillas_libres = False
                    break

            #Si  las casillas estaban vacías, colocamos el barco
            if casillas_libres:
                for x, y in coordenadas_barco:
                    tablero[x, y] = "🚢"  # marcamos la posición del barco
                #Añadimos al contador uno
                barcos_colocados += 1
                colocado = True   
    return tablero

#Disparar
def disparar(tablero, fila, columna):
    '''
    tablero = Tenemos que seleccionar el tablero del oponente
    fila = Indica la fila que queremos disparar
    columna = Indica la posicion de la columna a la que queremos disparar
    '''
    #Si es barco
    if fila >= 9 or columna >= 9:
        print("El valor no es valido.")
        return tablero
    elif tablero[fila, columna] == "🚢":
        tablero[fila, columna] = "💀"
        print("¡Tocado!")
        return tablero
    #Si es agua
    elif tablero[fila, columna] == "🌊":
        tablero[fila, columna] = "🔴"
        print("¡Agua!")
        return tablero
    #Si ya ha tocado
    elif tablero[fila, columna] == "🔴":
        tablero[fila, columna] = "🔴"
        print("Ya has elegido esta fila y columna anteriormente.")
        return tablero
    #Si ya ha matado
    elif tablero[fila, columna] == "💀":
        tablero[fila, columna] = "💀"
        print("Ya has elegido esta fila y columna anteriormente.")
        return tablero
    else:
        print("Error.")
        return tablero
