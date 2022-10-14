def suma_recursiva(l,s,n_d,multi):
    if n_d == 0:
        return s,multi
    else:
        if (n_d-1) % 2 == 0:
            s += l[n_d-1]
        else:
            multi *= l[n_d-1]
        return suma_recursiva(l,s,n_d-1,multi)

def elementos(n_d):
    l = []
    for e in range (n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def suma(l):
    suma = 0
    multi = 1
    for i in range(len(l)):
        if i % 2 == 0:
            suma += l[i]
        else:
            multi *= l[i]
    return suma,multi

def main():
    n_d = int(input("Ingrese el número total de datos que desea sumar: "))
    l = elementos(n_d)
    print("La suma de los valores de la lista es igual a:" , suma_recursiva(l,0,n_d,1))

main()