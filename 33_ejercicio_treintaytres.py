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

def mcd(n_d):
    l = elementos(n_d)
    l = sort(l)
    r = 1
    i = 2
    flag = True
    while i <= l[0]:
        for n in range(len(l)):
            if l[n] % i != 0:
                flag = False
        if flag:
            r *= i
            for n in range(len(l)):
                l[n] = l[n] / i
        else:
            flag = True
            i += 1
    return r

def mcd_recursiva(l,r,i):
    if i > l[0]:
        return r
    else:
        flag = True
        div = []
        for n in range(len(l)):
            div.append(l[n] / i)
            if l[n] % i != 0:
                flag = False
        if flag:
            l = div.copy()
            r *= i
            return mcd_recursiva(l,r,i) 
        else:
            return mcd_recursiva(l,r,i+1)

def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista a los que le quiere sacar el MCD: "))
    l = elementos(n_d)
    print("El máximo común divisor de los números ingresados es" , mcd_recursiva(l,1,2))

main()