def crea_matriz():
    F = int(input("- Ingrese el número de filas de su matriz: "))
    C = int(input("- Ingrese el número de columnas de su matriz: "))
    m= []
    for f in range(F):
        fila = []
        for c in range(C):
            e = int(input(" * Ingrese el elemento que corresponde a la columna " +str(c+1)+ " de la fila " +str(f+1) + ": " ))
            fila.append(e)
        m.append(fila)
    return m

def imprime_matriz(m):
    for f in range(len(m)):
        print("\n")
        for c in range(len(m[0])):
            print(m[f][c], " " , end="")
    print("\n")

def may_mey(m,n):
    for f in range(len(m)):
        for c in range(len(m[0])):
            if m[f][c] <= n:
                m[f][c] = 0
            else:
                m[f][c] = 1
    return m

def main():
    m = crea_matriz()
    n = int(input("Ingrese el número con el que desea comparar los elementos de la matriz: "))
    imprime_matriz(may_mey(m,n))

main()