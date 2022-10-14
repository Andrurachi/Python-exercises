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

def suma_columna(m,C):
    suma = 0
    for c in range (len(m)):
        suma += m[c][C-1]
    return suma

def main():
    m = crea_matriz()
    C = int(input("Ingrese la columna que desea sumar: "))
    print(suma_columna(m,C))

main()