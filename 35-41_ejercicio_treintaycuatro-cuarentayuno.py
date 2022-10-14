def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def sort(l):
    for i in range(len(l)):
        for n in range(len(l)):
            if l[i]<l[n]:
                l[i],l[n]=l[n],l[i]
    return l

def en(c,e):
    i = 0
    flag = False
    while i < len(c) and flag == False:
        if c[i] == e:
            flag = True
        i += 1
    return flag

def union(c_uno,c_dos):
    c_s = c_uno.copy()
    for i in range(len(c_dos)):
        if en(c_s,c_dos[i]) == False:
            c_s.append(c_dos[i])
    return sort(c_s)

def interseccion(c_uno,c_dos):
    c_i = []
    for i in range(len(c_dos)):
        if en(c_uno,c_dos[i]):
            c_i.append(c_dos[i])
    return sort(c_i)

def diferencia(c_uno,c_dos):
    c_d = []
    for i in range(len(c_uno)):
        if en(c_dos,c_uno[i]) == False:
            c_d.append(c_uno[i])
    return sort(c_d)

def diferencia_simetrica(c_uno,c_dos):
    c_union = union(c_uno,c_dos)
    c_inter = interseccion(c_uno,c_dos)
    return diferencia(c_union,c_inter)

def contiene(c_uno,c_dos):
    i = 0
    flag = True
    while i < len(c_dos) and flag:
        flag = en(c_uno,c_dos[i]) 
        i += 1
    return flag

def main():
    print("Bienvenido al analizador de conjuntos.")
    o = int(input("Ingrese la operación que desea realizar (Unión = 1, Intersección = 2, Diferencia = 3, Diferencia Simétrica = 4, Pertenece = 5, Contiene = 6): "))
    n_d_uno = int(input("Ahora ingrese el número de datos del primer conjunto: "))
    n_d_dos = int(input("Y ahora ingrese el número de datos del segundo conjunto: "))
    c_uno = elementos(n_d_uno)
    c_dos = elementos(n_d_dos)
    while o != 7:
        if o == 1:
            print("La unión de los conjuntos ingresados es:" , union(c_uno,c_dos))
        elif o == 2:
            print("La intersección de los conjuntos ingresados es:" , interseccion(c_uno,c_dos))
        elif o == 3:
            print("La diferencia del primer conjunto con el segundo conjuntos ingresados es:" , diferencia(c_uno,c_dos))
        elif o == 4:
            print("La diferencia simétrica de los conjuntos ingresados es:" , diferencia_simetrica(c_uno,c_dos))
        elif o == 5:
            e = int(input("Ingrese el entero que desea buscar: "))
            if en(c_uno,e) and en(c_dos,e):
                print("El entero pertenece a los dos conjuntos.")
            elif en(c_uno,e):
                print("El entero solo pertenece al primer conjunto.")
            elif en(c_dos,e):
                print("El entero solo pertenece al segundo conjunto.")
            else:
                print("El entero no pertenece a ningún conjunto.")
        elif o == 6:
            if contiene(c_uno,c_dos):
                print("El segundo conjunto sí esta contenido en el primero.")
            else:
                print("El segundo conjunto no esta contenido en el primero.")
        else:
            print("El número de operación ingresado no es válido, intente nuevamente.")
        
        o = int(input("Ingrese nuevamente la operación que desea realizar o ingrese 7 para salir (Unión = 1, Intersección = 2, Diferencia = 3, Diferencia Simétrica = 4, Pertenece = 5, Contiene = 6): "))
    return "Gracias por preferirnos."

main()