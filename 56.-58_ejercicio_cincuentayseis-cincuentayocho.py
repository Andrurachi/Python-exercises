def crea_matriz():
    F = int(input("- Ingrese el número de filas de su matriz: "))
    C = int(input("- Ingrese el número de columnas de su matriz: "))
    m= []
    for f in range(F):
        fila = []
        for c in range(C):
            e = float(input("   * Ingrese el elemento que corresponde a la columna " +str(c+1)+ " de la fila " +str(f+1) + ": " ))
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

def supermatriz(m,m_ide,vec):
    super_m = m.copy()
    for f in range(len(m_ide)):
        for c in range(len(m_ide[0])):
            super_m[f].append(m_ide[f][c])
        super_m[f].append(vec[f])
    return super_m

def identidad(f):
    m_i = matriz_nula(f,f)
    for i in range(f):
        m_i[i][i] = 1
    return m_i

def div_fila(f,d):
    F = f.copy()
    for c in range(len(F)):
        F[c] = (F[c]/d)
    return F

def multi_fila(f,m):
    F = f.copy()
    for c in range(len(F)):
        F[c] = (F[c]*m)
    return F

def resta_filas(f_uno,f_dos):
    F = f_uno.copy()
    for c in range(len(f_uno)):
        F[c] = (F[c]-f_dos[c])
    return F

def separa(s_m):
    x = []
    m_i = matriz_nula(len(s_m),len(s_m))
    for f in range(len(m_i)):
        x.append(s_m[f][len(s_m[0])-1])
        for c in range(len(m_i)):
            m_i[f][c] = s_m[f][c+len(m_i)]
    return x,m_i

m = [[1,1,1],
     [1,0,0],
     [0,1,0]]

def reduccion_gauss(m,v):
    d = 1 #valor inicial determinante
    m_i = identidad(len(m)) #Matriz identidad y futura matriz inversa
    s_m = supermatriz(m,m_i,v)
    for piv in range (len(s_m)):
        if s_m[piv][piv] == 0: #Si el pivote es 0
            i = 1
            while s_m[piv][piv] == 0 and i < len(s_m)-piv: #cambiar filas mientras el pivote sea cero sin pasar el número de filas
                s_m[piv] , s_m[piv+i] = s_m[piv+i].copy() , s_m[piv].copy() 
                d *= -1 #Cambiar el signo de la determinante por cada cambio
                i += 1
        if s_m[piv][piv] != 1: #Si el pivote es diferente de uno
            d *= s_m[piv][piv]
            s_m[piv] = div_fila(s_m[piv],s_m[piv][piv]) #Dividir toda la fila por el pivote para que este sea uno
        for f in range(len(s_m)):
            if f != piv and s_m[f][piv] != 0: # Analizar la columna del pivote para que no tenga valores diferentes de cero
                f_m = multi_fila(s_m[piv],s_m[f][piv]) #Crea una fila que se le  restará a la fila en cuestión para transformar en cero
                s_m[f] = resta_filas(s_m[f],f_m)
    x,m_i = separa(s_m)
    return x,m_i,d

def main():
    print("Bienvenido. Acá podrás usar la reducción de Gauss/Jordan para diferentes fines.")
    print("- Igrese 1 para hallar la determinante de una matriz.")
    print("- Ingrese 2 para hallar las x de un sistema de ecuaciones como matriz.")
    print("- Ingrese 3 para hallar la matriz inversa de una matriz cuadrada.")
    o = int(input("Ingrese la opción que desee: "))
    while o != 4:
        if o == 1:
            print("\n")
            print("Ingresa la matriz de la que deseas conocer conocer la determinante.")
            m = crea_matriz()
            v = []
            for i in range(len(m)):
                v.append(0)
            if len(m) != len(m[0]):
                print("La matriz ingresada no es una matriz cuadrada.")
            else:
                x,m_iv,d = reduccion_gauss(m,v)
                print("\n")
                print("LA DETERMINANTE DE LA MATRIZ ES:   " , d)
                print("\n")
        elif o == 2:
            print("\n")
            print("Ingresa la matriz que corresponde al sitema de ecuaciones (no incluyas el vector al otro lado del igual).")
            m = crea_matriz()
            v = []
            for i in range(len(m)):
                e = float(input("- Ingrese a lo que se iguala la ecuación " + str(i+1) + " (correspondiente a la fila " + str(i+1) + " de la matriz): "))
                v.append(e)
            if len(m) != len(m[0]):
                print("La matriz ingresada no es una matriz cuadrada.")
            else:
                x,m_iv,d = reduccion_gauss(m,v)
                print("\n")
                print("LAS SOLUCIONES DE X DE LA ECUACIÓN INGRESADA SON (EN ORDEN):   " , x)
                print("\n")
        elif o == 3:
            print("\n")
            print("Ingresa la matriz de la cual deseas conocer su inversa.")
            m = crea_matriz()
            v = []
            for i in range(len(m)):
                v.append(0)
            x,m_iv,d = reduccion_gauss(m,v)
            print("\n")
            print("LA MATRIZ INVERSA DE LA MATRIZ INGRESADA ES:   ")
            imprime_matriz(m_iv)
            print("\n")
        else:
            o = int(input("La operación ingresada no es válida."))
        o = int(input("Ingrese nuevamente la operación que desea realizar o presione 4 para salir (1 = Determinante, 2 = Soluciones de X, 3 = Matriz inversa.): "))
    print("Gracias por preferirnos.")

main()