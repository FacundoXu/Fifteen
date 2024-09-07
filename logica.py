from random import *

# Tamaño
FILAS = 4
COLUMNAS = 4

# Entradas
ARRIBA = 'w'
IZQUIERDA = 'a'
ABAJO = 's'
DERECHA = 'd'
CERRAR = 'o'
MOVIMIENTOS = (ARRIBA, IZQUIERDA, ABAJO, DERECHA)

# Otros
VACIO = ''
Z = randint(1, 50)
MAX_MOVIMIENTOS = Z * 5

# Diseño
SIMBOLOS = ''' 
╔══╗
║  ║
╚══╝
'''

GANAR = '¡VICTORIA!'

PERDER = 'PERDISTE, SUERTE PARA LA PROXIMA'

SALIR = 'SALISTE CON ÉXITO'

def crear_juego(filas, columnas):
    '''
    Recibe la cantidad de filas y columnas. Devuelve una lista que contiene los elementos del juego
    '''
    juego = []

    for n in range(1, filas * columnas):  
        juego.append(n) 

    juego.append(VACIO)
    juego.reverse()         
           
    return juego

def crear_tablero(filas, columnas, juego):
    '''
    Recibe la cantidad de filas, columnas y un juego. Devuelve una matriz que representa el tablero del juego
    '''
    tablero = [[juego.pop() for j in range(columnas)] for i in range(filas)]                             
    return tablero

def posicion_vacio(tablero):
    '''
    Recibe un tablero. Devuelve la posicion de la casilla vacia
    '''
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == VACIO:
                return i, j

def mover_tablero(tablero, entrada):
    '''
    Recibe un tablero y una entrada. Devuelve el mismo tablero modificado con respecto a la entrada ingresada
    '''
    i, j = posicion_vacio(tablero)

    if entrada == ARRIBA and i != FILAS - 1:
            tablero[i][j], tablero[i + 1][j] = tablero[i + 1][j], tablero[i][j]            
    if entrada == IZQUIERDA and j != COLUMNAS - 1:
            tablero[i][j], tablero[i][j + 1] = tablero[i][j + 1], tablero[i][j]    
    if entrada == ABAJO and i != 0:
            tablero[i][j], tablero[i - 1][j] = tablero[i - 1][j], tablero[i][j]   
    if entrada == DERECHA and j != 0:
            tablero[i][j], tablero[i][j - 1] = tablero[i][j - 1], tablero[i][j]    
        
    return tablero

def generar_movimientos_aleatorios():
    '''
    Devuelve una lista con movimientos aleatorios
    '''
    movimientos_aleatorios = []

    for i in range(Z):
        movimientos_aleatorios.append(choice(MOVIMIENTOS))

    return movimientos_aleatorios

def copiar_tablero(tablero):
    '''
    Devuelve una copia del tablero original
    '''
    tablero_copia = []

    for i in range(len(tablero)):
        tablero_copia.append(tablero[i].copy())

    return tablero_copia

def desordenar_tablero(tablero):
    '''
    Recibe un tablero. Devuelve un tablero desordenado utilizando como referencia una lista de movimientos aleatorios
    '''
    tablero_copia = copiar_tablero(tablero)
    movimientos_aleatorios = generar_movimientos_aleatorios()
    
    for movimiento in movimientos_aleatorios:
        mover_tablero(tablero_copia, movimiento)

    return tablero_copia

def imprimir_tablero(tablero):
    '''
    Imprime un tablero con sus respectivos elementos
    '''
    print()
    print('╔═════ FIFTEEN ═════╗')

    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            print('║' + str(tablero[i][j]).center(3), end=' ')
        print('║')
        
    print('╚═══════════════════╝')

def imprimir_controles():
    '''
    Imprime los controles del juego
    '''
    print('Controles: w, a, s, d')
    print('Salir del juego: o')

def imprimir_movimientos(movimientos):
    '''
    Imprime la cantidad de movimientos realizados
    '''
    print('Movimientos realizados:', movimientos, '/', MAX_MOVIMIENTOS)

def pedir_movimiento():
    '''
    Pide una entrada al usuario
    '''
    entrada = input('Entrada: ')

    return entrada

def estado_juego(tablero, tablero_resuelto, movimientos):
    '''
    Recibe un tablero, un tablero ordenado y la cantidad de movimientos. Devuelve True si el juego esta ganado y
    devuelve False si esta perdido
    '''
    if tablero == tablero_resuelto:
        return True
    if movimientos >= MAX_MOVIMIENTOS:
        return False