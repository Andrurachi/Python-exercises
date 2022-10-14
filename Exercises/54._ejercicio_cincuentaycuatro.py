def crea_matriz(cuadrada):
    if cuadrada:
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

def suma_fila(m,f):
    s = 0
    for c in range (len(m[0])):
        s += m[f-1][c]
    return s

def suma_columna(m,C):
    s = 0
    for c in range (len(m)):
        s += m[c][C-1]
    return s

def filas_columnas(m,s):
    flag = True
    i = 0
    while i < len(m) and flag:
        if suma_fila(m,i+1) != s or suma_columna(m,i+1) != s:
            flag = False
        else:
            i += 1
    return flag 

def diagonales(m,s):
    flag = True
    d_uno , d_dos = 0 , 0 
    for i in range(len(m)):
        d_uno += m[i][i]  
        d_dos += m[i][len(m)-(i+1)]
    if d_uno != s or d_dos != s:
        flag = False
    return flag

def main():
    m = crea_matriz()
    s = suma_fila(m,0)
    if filas_columnas(m,s) and diagonales(m,s):
        print("Es una matriz mágica.")
    else:
        print("No es una matriz mágica.")

main()