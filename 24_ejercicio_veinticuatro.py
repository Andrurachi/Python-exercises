def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def sumar(l):
    suma = 0
    for i in range(len(l)):
        suma += l[i]
    return suma

def promedio(n_d):
    l = elementos(n_d)
    return sumar(l)/n_d

def main():
    n_datos = int(input("Ingrese el número total de datos a los que le sacará el promedio: "))
    print("El promedio de loso elementos de la lista es:" , promedio(n_datos))

main()