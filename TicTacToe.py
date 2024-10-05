from random import randrange
varJugador = "X"
lugar = 5
winner = "nadie"
resultado = []
jugada = 0


# 1.Pinta tablero Inicial: Crea Tabla resultado
def inicio():  
   contador = 0  
   for i in range(3):
        list=[]
        for j in range(3):
            contador += 1
            if contador == 5:
                list.append(varJugador)
            else:
              list.append(contador)
            if contador % 3 == 0:
                resultado.append(list.copy())  # no queda referenciada

inicio()

# 2.Pinta Tablas nuevas despues de cada jugada
def pinta():
    for fila in range(len(resultado)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {resultado[fila][0]}   |   {resultado[fila][1]}   |   {resultado[fila][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

pinta()

#3.Aquí se pregunta al usuario la jugada y se evalua si se puede
def jugada():
    intento = False
    jugada += 1
    index
    pos

    # 3.1 esta funcion evalua si el numero introducido por ususario es correcto
    def check(numero):
        indice
        posicion
        for i in range(len(resultado)):
            for j in range(len(resultado[i])):#va uno por uno
                if resultado[i][j]== numero:#si existe el numero en el juego
                    indice= i
                    posicion = j
                    intento = True #si sirve el numero para la jugada
                    return (indice,posicion,intento)# se sale de la f(x)
                
        return (indice,posicion,intento) #intento sigue siendo false

    #3.2 Solicitud de informacion y/o numero random
    while intento == False:

        if jugada % 2 == 0: #Si el numero es par, juega usuario
            varJugador = "O"
            lugar = input ("\nIngresa tu movimiento: ")
            index,pos,intento = check(lugar)

        else:
            varJugador = "X"
            lugar= randrange(1,9)
            print(f"el pc eligió {lugar}")
            index,pos,intento = check(lugar)
    
    #3.2. Modificará el resultado cuando salga del while
    resultado[index][pos]= varJugador 
#falta check

#4. Evaluación de la Jugada (Ver si existe un ganador)
def evaluacion():
    #4.1 Análisis Horizontal
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila
        for j in range(len(resultado[i])): # Recorremos cada columna
            if resultado[i][j] == varJugador: #analisis de fila
                contador += 1
                print(f"Jugada Horizontal:{contador}")
            
            if contador == 3:
                winner = "¡Has Ganado!"
                return winner #Sale de def evaluacion
            
        contador = 0 #esto analizara la proxima fila 

    
    #4.2 Análisis Vertical
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila por índice
        for j in range(len(resultado[i])):# 3 casillas horizontales
            if resultado[j][i] == varJugador: #resultado[0][0], resultado[1]][0], resultado[2][0] tienen x
                contador +=1
                print(f"Jugada Vertical:{contador}")

            if contador == 3:
                winner = "¡Has Ganado!"
                return winner #Sale de def evaluacion
            
        contador = 0 #esto analizara la proxima fila 

    #4.3 Análisis Diagonal1 mas parecidas entre ellas
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila por índice
        for j in range(len(resultado[i])):# osea 3 casillas horizontales
            if (i==j) and (resultado[i][j] == varJugador): #resultado[0][0], resultado[1]][1], resultado[2][2] tienen x
                contador +=1
                print(f"Jugada Diagonal1:{contador}")
                
                if contador == 3:
                    winner = "¡Has Ganado!"
                    return winner #Sale de def evaluacion
            
    #4.4 Análisis Diagonal2 mas parecidas entre ellas y LA HORIZONTAL Y VERTICAL JUNTAS
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila por índice
        for j in range(len(resultado[i])):# osea 3 casillas horizontales
            if (i+j == 2) and (resultado[i][j] == "x"): #resultado[0][0], resultado[1]][1], resultado[2][2] tienen x
                contador +=1
                print(f"Jugada Diagonal2:{contador}")
                
                if contador == 3:
                    winner = "¡Has Ganado!"
                    return winner #Sale de def evaluacion
                
    #4.5 Chequedo de Empate
    for fila in range(len(resultado)): # Recorremos cada fila por índice
        for col in range(len(resultado[fila])):# osea 3 casillas horizontales
            if col != "X" and col != "O" #Si es un número
                winner = "nadie"
                return winner #"nadie"
    
    winner = "Empate"        
    return winner
        
        
