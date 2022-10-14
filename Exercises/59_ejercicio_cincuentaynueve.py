def imprime_matriz(m):
    for f in range(len(m)):
        print("\n")
        for c in range(len(m[0])):
            print(m[f][c], " " , end="")
    print("\n")

def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def matriz_nula(f): # f son las filas
    m_n = []
    for i in range(f):
        fila = []
        for n in range(f):
            fila.append(0)
        m_n.append(fila)
    return m_n

def espiral(l):
    m = matriz_nula(int(len(l)**0.5))
    if len(m) % 2 != 0:
        v = len(m)//2 + 1
    else:
        v = len(m)//2 
    for t in range (v): #por cada turno disminuye el doble de turno para no modificar las mismas posiciones
        if len(l) == 1:
            m[len(m)//2][len(m)//2] = l[0]
            l.pop(0)
        else:
            for c in range(len(m)-t*2): #Primera fila (Se desplaza por columnas)
                m[t][c+t] = l[0]
                l.pop(0)
            for f in range(len(m)-t*2-1): #Última columna (Se desplaza por filas sin contar la primera porque ya fue modificada)
                m[f+t+1][len(m)-1-t] = l[0]
                l.pop(0)
            for c in range(len(m)-2-t*2,-1,-1): #Última fila (Se desplaza por columnas al revés sin contar la última)
                m[len(m)-t-1][c+t] = l[0]
                l.pop(0)
            for f in range(len(m)-2-t*2,0,-1): #Primera columna (se desplaza por filas al revés sin contar ni la primera ni la última)
                m[f + t][0 + t] = l[0]
                l.pop(0)
    return m
                
def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista que desea organizar en espiral en una matriz: "))
    l = elementos(n_d)
    imprime_matriz(espiral(l))

main()