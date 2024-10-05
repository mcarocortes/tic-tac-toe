varJugador = "x"
lugar = 5
winner = "nadie"
resultado = []
jugada = 0


# Pinta tablero Inicial: Crea Tabla resultados
def inicio():  
   contador = 0  
   for i in range(3):
        list=[]
        for j in range(3):
            contador += 1
            if contador == 5:
                list.append("x")
            else:
              list.append(contador)
            if contador % 3 == 0:
                resultado.append(list.copy())  # no queda referenciada

inicio()

#Pinta Tablas nuevas despues de cada jugada
def pinta():
    for fila in range(len(resultado)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {resultado[fila][0]}   |   {resultado[fila][1]}   |   {resultado[fila][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

pinta()

#Aquí se pregunta al usuario la jugada y se evalua si se puede
def jugada():
    intento = False
    jugada += 1

    def check(numero):#esta funcion es para ver si el numero introducido por ususario es 

