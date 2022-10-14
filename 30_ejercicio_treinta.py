def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos de la lista a organizar: "))
        l.append(e)
    return l

def ordenar_ceros(n_d):
    l  = elementos(n_d)
    l_o = []
    ceros = 0
    for i in range(n_d):
        if l[i] == 0:
            ceros += 1
        else:
            l_o.append(l[i])
    for i in range(ceros):
        l_o.append(0)
    return l_o

def ordenar_ceros_recursiva(l,i,c): #No sirve :c
    if i >= len(l)-1-c:
        return l
    elif l[i] == 0:
        c += 1
        for n in range(i,len(l)-1):
            l[n],l[n+1] = l[n+1],l[n]
        return ordenar_ceros_recursiva(l,i,c)
    else:
        return ordenar_ceros_recursiva(l,i+1,c) 

def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista en la que quiere dejar de últmas los ceros: "))
    l = elementos(n_d)
    print("El nuevo orden de la lista es: " , ordenar_ceros_recursiva(l,0,0))
main()