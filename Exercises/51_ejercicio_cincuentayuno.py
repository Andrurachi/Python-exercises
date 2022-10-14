def multiplicar(m_uno,m_dos):
    m_multi = []
    for i in range(len(m_uno)):
        turno_uno , a_multi = m_uno[i] , []
        for n in range (0 , len(m_dos[i])):
            turno_dos , multi_turno = [] , 0
            for d in range (0 , len(turno_uno)):
                matriz_turno = m_dos[d] 
                turno_dos.append(matriz_turno[n])
            for z in range (0,len(turno_uno)):
                multi_turno += (turno_uno[z] * turno_dos[z])
            a_multi.append(multi_turno)
        m_multi.append(a_multi)
    return m_multi

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

def matriz_nula(f,c):
    m_n = []
    for i in range(f):
        fila = []
        for n in range (c):
            fila.append(0)
        m_n.append(fila)
    return m_n

def multiplicar2(m_uno,m_dos):
    m_m = matriz_nula(len(m_uno),len(m_dos[0]))
    for f in range(len(m_m)):
        for c in range(len(m_m[0])):
            for i in range(len(m_dos)):
                m_m[f][c] += m_uno[f][i] * m_dos[i][c]
    return m_m

def main():
    m_uno = crea_matriz()
    m_dos = crea_matriz()
    imprime_matriz(multiplicar2(m_uno,m_dos))

main()