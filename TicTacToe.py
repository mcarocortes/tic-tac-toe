from random import randrange
varJugador = "X"
lugar = 5
winner = "Nadie"
resultado = []



# 1.Pinta tablero Inicial: Crea Tabla resultado
def Inicio():  
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


# 2.Pinta Tablas nuevas despues de cada jugada
def Pinta():
    for fila in range(len(resultado)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {resultado[fila][0]}   |   {resultado[fila][1]}   |   {resultado[fila][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


#3.Aquí se pregunta al usuario la jugada y se evalua si se puede
def Jugar(jugada):
    global intento
    intento = False
    jugada += 1
    global index
    global pos

    # 3.1 esta funcion evalua si el numero introducido por ususario es correcto
    def Check(numero):
        global indice
        global posicion
        for i in range(len(resultado)):
            for j in range(len(resultado[i])):#va uno por uno
                if resultado[i][j] == numero:#si existe el numero en el juego
                    indice= i
                    posicion = j
                    intento = True #si sirve el numero para la jugada
                    return (indice,posicion,intento)# se sale de la f(x)
                
        return (indice,posicion,intento) #intento sigue siendo false

    #3.2 Solicitud de informacion y/o numero random
    while intento == False:

        if jugada % 2 == 0: #Si el numero es par, juega usuario
            varJugador = "O"
            lugar = int(input ("\nIngresa tu movimiento: "))
            index,pos,intento = Check(lugar)

        else:
            varJugador = "X"
            lugar= randrange(1,9)
            print(f"el pc eligió {lugar}")
            index,pos,intento = Check(lugar)
    
    #3.2. Modificará el resultado cuando salga del while
    resultado[index][pos]= varJugador 
#falta check

#4. Evaluación de la Jugada (Ver si existe un ganador)
def Evaluacion():
    #4.1 Análisis Horizontal
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila
        for j in range(len(resultado[i])): # Recorremos cada columna
            if resultado[i][j] == varJugador: #analisis de fila
                contador += 1
                print(f"Jugada Horizontal:{contador}")
            
            if contador == 3:
                winner = "¡Ganador!"
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
                winner = "¡Ganador!"
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
                    winner = "Ganador"
                    return winner #Sale de def evaluacion
            
    #4.4 Análisis Diagonal2 mas parecidas entre ellas y LA HORIZONTAL Y VERTICAL JUNTAS
    contador = 0
    for i in range(len(resultado)): # Recorremos cada fila por índice
        for j in range(len(resultado[i])):# osea 3 casillas horizontales
            if (i+j == 2) and (resultado[i][j] == "x"): #resultado[0][0], resultado[1]][1], resultado[2][2] tienen x
                contador +=1
                print(f"Jugada Diagonal2:{contador}")
                
                if contador == 3:
                    winner = "Ganador"
                    return winner #Sale de def evaluacion
                
    #4.5 Chequedo de Empate
    for fila in range(len(resultado)):  # Recorremos cada fila por índice
        for col in range(len(resultado[fila])):  # o sea 3 casillas horizontales
          if (resultado[fila][col] != "X" and resultado[fila][col] != "O"):  # Si es un número
                winner = "Nadie"
                return winner  # "Nadie"
    
    winner = "Empate"        
    return winner
        
        
#¡LETS PLAY!

Inicio()
Pinta()
jugada = 1

while winner == "Nadie":
    Jugar(jugada)
    Pinta()
    winner = Evaluacion()
    jugada +=1


if winner == "Ganador":
    print("\nFelicidades Has Ganado")
elif winner == "Empate":
    print("\nEmpatarooon")
