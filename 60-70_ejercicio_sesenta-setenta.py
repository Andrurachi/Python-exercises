def crea_matriz():
    F = int(input("Ingrese el número de filas de su matriz: "))
    C = int(input("Ingrese el número de columnas de su matriz: "))
    m= []
    for f in range(F):
        fila = []
        for c in range(C):
            e = int(input("Ingrese el elemento que corresponde a la columna " +str(c+1)+ " de la fila " +str(f+1) + ": " ))
            fila.append(e)
        m.append(fila)
    return m

def imprime_matriz(m):
    for f in range(len(m)):
        print("\n")
        for c in range(len(m[0])):
            print(m[f][c], " " , end="")
    print("\n")

def multi_booleana(m_uno,m_dos):
    m_m = matriz_nula(len(m_uno),len(m_dos[0]))
    for f in range(len(m_m)):
        for c in range(len(m_m[0])):
            for i in range(len(m_dos)):
                if m_uno[f][i] * m_dos[i][c] != 0:
                    m_m[f][c] = 1
    return m_m

def matriz_nula(f,c):
    m_n = []
    for i in range(f):
        fila = []
        for n in range(c):
            fila.append(0)
        m_n.append(fila)
    return m_n

def union(m_uno,m_dos):
    m_u = matriz_nula(len(m_uno),len(m_uno[0]))
    for f in range (len(m_uno)):
        for c in range(len(m_uno[0])):
            if m_uno[f][c] == 1 or m_dos[f][c] == 1:
                m_u[f][c] = 1
    return m_u

def interseccion(m_uno,m_dos):
    m_i = matriz_nula(len(m_uno),len(m_uno[0]))
    for f in range (len(m_uno)):
        for c in range(len(m_uno[0])):
            if m_uno[f][c] == 1 and m_dos[f][c] == 1:
                m_i[f][c] = 1
    return m_i

def simetria(m):
    flag = True
    if len(m) != len(m[0]):
        flag = False
    f = 0
    while f < len(m) and flag:
        c = 0
        while c < len(m[0])-f and flag:
            if m[f][c+f] != m[c+f][f]:
                flag = False
            c += 1
        f += 1
    return flag

def reflexibidad(m):
    flag = True
    if len(m) != len(m[0]):
        flag = False
    i = 0
    while i < len(m) and flag:
        if m[i][i] == 0:
            flag = False
        i += 1
    return flag

def transitividad (m_1): #Corregir comparación
    a = m_1.copy()
    m_cuadrada = multi_booleana(a,a)
    if m_cuadrada <= a:
        return True
    else:
        return False

def transitividad2(m):
    flag = True
    f = 0
    while f < len(m) and flag:
        c = 0
        while c < len(m[0]) and flag:
            n = 0
            if  m[f][c] == 1:
                while n < len(m) and flag:
                    if m[c][n] == 1 and m[f][n] == 0:
                        flag = False
                    n += 1
            c += 1
        f += 1
    return flag

def antisimetria(m):
    flag = True
    if len(m) != len(m[0]):
        flag = False
    f = 0
    while f < len(m) and flag:
        c = 0
        while c < len(m[0])-f and flag:
            if f != c+f and m[c+f][f] != 0 and m[f][c+f] == m[c+f][f]:
                flag = False
            c += 1
        f += 1
    return flag

def orden(m):
    if reflexibidad(m) and transitividad(m) and antisimetria(m):
        return True
    else:
        return False

def equivalencia(m):
    if reflexibidad(m) and transitividad(m) and simetria(m):
        return True
    else:
        return False

def funcion(m):
    flag = True
    f = 0
    while f < len(m) and flag:
        s_f = 0 #Suma de la fila
        for c in range(len(m[0])):
            s_f += m[f][c]
        if s_f > 1: # Cada "x" puede tener máximo una "y"
            flag = False
        f += 1
    return flag

def inyectiva(m):
    flag = True
    if funcion(m):
        f = 0
        while f < len(m) and flag:
            s_c = 0
            for c in range(len(m[0])):
                s_c += m[c][f]
            if s_c > 1: # Cada "y" puede tener máximo una "x"
                 flag = False
            f += 1
    else:
        flag = False
    return flag

def sobreyectiva(m):
    flag = True
    if funcion(m):
        f = 0
        while f < len(m) and flag:
            s_c = 0
            for c in range(len(m[0])):
                s_c += m[c][f]
            if s_c < 1: # Cada "y" puede tener mínimo una "x"
                 flag = False
            f += 1
    else:
        flag = False
    return flag

def main():
    print("Bienvenido al analizador de relaciones de conjuntos como matrices.")
    o = int(input("Ingrese la operación o el análisis que desea realizar (Del 3-10 es con la primera relación) (Unión = 1, Intersección = 2, Simetría = 3, Reflexividad = 4, Transitividad = 5, Orden = 6, Equivalencia = 7, Función = 8, Inyectiva = 9, Sobreyectiva = 10): "))
    m_1 = crea_matriz()
    m_2 = crea_matriz()
    while o != 11:
        if o == 1:
            if len(m_1) != len(m_2):
                print("No se pueden sumar las relaciones porque son de diferentes conjuntos.")
            else:
                imprime_matriz(union(m_1,m_2))
        elif o == 2:
            if len(m_1) != len(m_2):
                print("No se puede hallar la intersección de las relaciones porque son de diferentes conjuntos.")
            else:
                imprime_matriz(interseccion(m_1,m_2))
        elif o == 3:
            if simetria(m_1):
                print("Es relación simétrica.")
            else:
                print("No es relación simétrica.")
        elif o == 4:
            if reflexibidad(m_1):
                print("Es relación reflexiva.")
            else:
                print("No es relación reflexiva.")
        elif o == 5:
            if transitividad2(m_1):
                print("Es relación transitiva.")
            else:
                 print("No es relación transitiva.")
        elif o == 6:
            if orden(m_1):
                print("Es relación de orden.")
            else:
                print("No es relación transitiva.")
        elif o == 7:
            if equivalencia(m_1):
                print("Es relación equivalente.")
            else:
                print("No es relación equivalente.")
        elif o == 8:
            if funcion(m_1):
                print("Es función.")
            else:
                print("No es función.")
        elif o == 9:
            if inyectiva(m_1):
                print("Es función inyectiva.")
            else:
                print("No es función inyectiva.")
        elif o == 10:
            if sobreyectiva(m_1):
                print("Es función sobreyectiva.")
            else:
                print("No es función sobreyectiva.")
        else:
            print("El número de operación o análisis ingresado no es válido.")   
        o = int(input("Ingrese nuevamente la operación o el análisis que desea realizar o ingrese 11 para salir del programa (Unión = 1, Intersección = 2, Simetría = 3, Reflexividad = 4, Transitividad = 5, Orden = 6, Equivalencia = 7, Función = 8, Inyectiva = 9, Sobreyectiva = 10): "))
    return "Gracias por preferirnos."

main()