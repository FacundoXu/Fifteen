from logica import *

def main():
    juego_resuelto = crear_juego(FILAS, COLUMNAS)
    tablero_resuelto = crear_tablero(FILAS, COLUMNAS, juego_resuelto)
    tablero = desordenar_tablero(tablero_resuelto)
    movimientos = 0
    
    while True:
        imprimir_tablero(tablero)
        imprimir_controles()
        imprimir_movimientos(movimientos)

        entrada = pedir_movimiento()
        mover_tablero(tablero, entrada)
        
        movimientos += 1
        estado_del_juego = estado_juego(tablero, tablero_resuelto, movimientos)

        if estado_del_juego == True:
            imprimir_tablero(tablero)
            print(GANAR)
            break

        if estado_del_juego == False:
            print(PERDER)
            break

        if entrada == CERRAR:
            print(SALIR)
            break

main()