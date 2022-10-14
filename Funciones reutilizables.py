def contar(C,c): #sustituto .count()
    count = 0
    for i in range (len(C)):
        if C[i] == c:
            count += 1
    return count

def delete(C,c): #sustituto .remove() para cadenas
    C_f = "" 
    flag = True
    for i in range(len(C)):
        if C[i] == c and flag:
            flag = False
        else:
            C_f += C[i]
    return C_f

def delete_all(C,c): # Remover por completo determinado carácter de una cadena
    C_f = ""
    for i in range(len(C)):
        if C[i] != c:
            C_f += C[i]
    return C_f

def en(c,e): #sustituto in
    i = 0
    flag = False
    while i < len(c) and flag == False:
        if c[i] == e:
            flag = True
        i += 1
    return flag

def repetidos(C): #Quitar elementos repetidos de una cadena (requiere en())
    C_f = ""
    for i in range (len(C)):
        if en(C_f,C[i]) == False:
            C_f += C[i]
    return C_f

def elementos(n_d): #Pedir elementos para crear un arreglo
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def reverse(l): #Sustituto de .reverse()
    l_f = []
    for i in range(len(l)-1,-1,-1):
        l_f.append(l[i])
    return l_f

def sort(l): #Sustituto de .sort()
    for i in range(len(l)):
        for n in range(len(l)):
            if l[i]<l[n]:
                l[i],l[n]=l[n],l[i]
    return l

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