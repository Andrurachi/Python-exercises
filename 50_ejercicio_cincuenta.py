def sumar(m_uno,m_dos):
    m_suma = []
    for i in range (0 , len(m_uno)):
        m_turno_uno , m_turno_dos , m_turno_suma = m_uno[i] , m_dos[i] , []
        for n in range (0 , len(m_turno_uno)):
            m_turno_suma.append(m_turno_uno[n] + m_turno_dos[n])
        m_suma.append(m_turno_suma)
    return m_suma

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
        for n in range(c):
            fila.append(0)
        m_n.append(fila)
    return m_n

def sumar2(m_uno,m_dos):
    m_s = matriz_nula(len(m_uno),len(m_uno[0]))
    for f in range(len(m_uno)):
        for c in range(len(m_uno[0])):
            m_s[f][c] = m_uno[f][c] + m_dos[f][c]
    return m_s

def main():
    m_uno = crea_matriz()
    m_dos = crea_matriz()
    m_s = sumar2(m_uno,m_dos)
    print("\n")
    print("LA MATRIZ SUMA ES:")
    imprime_matriz(m_s)

main()

