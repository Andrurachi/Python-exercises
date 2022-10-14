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

def medianas(n_d):
    l = elementos(n_d)
    sort(l)
    mitad = n_d // 2
    if n_d % 2 == 0:
        return (l[mitad-1] + l[mitad]) / 2
    else:
        return (l[mitad])

def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista a la que le quiere sacar la mediana: "))
    print("la mediana es: " , medianas(n_d))

main()