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

def maximo(n_d):
    l = elementos(n_d)
    sort(l)
    return l[n_d-1]
        
def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista de la que desea sacar el de mayor valor: "))
    print("El número de mayor valor de la lista es de" , maximo(n_d))

main()