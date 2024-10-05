from random import randrange
varJugador = "X"
lugar = 5
winner = "nadie"
resultado = []
jugada = 0


# 1.Pinta tablero Inicial: Crea Tabla resultados
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
    
    #4. Modificará el resultado cuando salga del while
    resultado[index][pos]= varJugador