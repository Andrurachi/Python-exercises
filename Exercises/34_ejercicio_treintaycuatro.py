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

def mcm(n_d):
    l = elementos(n_d)
    l = sort(l)
    r = 1
    i = 2
    flag = False
    while i <= l[len(l)-1]:
        for n in range(len(l)):
            if l[n] % i == 0:
                l[n] = l[n]/i
                flag = True
        if flag:
            r *= i
            flag = False
        else:
            i += 1
        sort(l)
    return r

def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista a los que le quiere sacar el MCM: "))
    print("El mínimo común múltiplo de los números ingresados es" , mcm(n_d))

main()