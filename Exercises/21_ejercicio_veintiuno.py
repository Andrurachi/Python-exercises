def combinaciones(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t == 2:
        return 2
    else:
        return combinaciones(t - 1) + combinaciones(t - 2)

def combinaciones_amarillas(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t == 2:
        return 2
    elif t == 3:
        return 4
    else:
        return combinaciones_amarillas(t - 1) + combinaciones_amarillas(t - 2) + combinaciones_amarillas(t - 3) 

def combinaciones_amarillas_mas(t):
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t == 2:
        return 2
    elif t == 3:
        return 4
    elif t == 4:
        return 8
    else:
        return combinaciones_amarillas_mas(t - 1) + combinaciones_amarillas_mas(t - 2) + combinaciones_amarillas_mas(t - 3) + combinaciones_amarillas_mas(t - 4)

def main():
    t = int(input("Ingrese el número de centímetros que tiene el tablero de largo: "))
    print("El número de formas distintas que puede ubicar las fichas sobre el tablero es de" , combinaciones(t), " y con fichas amarillas sería entonces" , combinaciones_amarillas(t))

main()