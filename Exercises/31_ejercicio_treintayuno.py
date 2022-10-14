def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def decimal (n_d):
    b = elementos(n_d)
    d = 0
    e = 0
    for i in range (n_d-1,-1,-1):
        d += b[i] * (2 ** (e))
        e += 1
    return d

def main():
    n_d = int(input("Ingrese el número de datos que tiene la lista donde se encuentra el número en binario que desea conocer en decimal: "))
    print("El número en decimal es" , decimal(n_d))
 
main()