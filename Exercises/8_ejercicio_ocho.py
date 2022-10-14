def primos_relativos_recursiva(n_uno,n_dos,i):
    if i == n_dos:
        return True
    elif n_uno % i == 0 and n_dos % i == 0:
        return False
    else:
        return primos_relativos_recursiva(n_uno,n_dos,i+1)

def primos_relativos(n_uno,n_dos):
    flag = True
    i = 2
    while i <= n_dos and flag:
        if n_uno % i == 0 and n_dos % i == 0:
            flag = False
        i += 1
    return flag

def main():
    n_uno = float(input("Ingrese el primer número a analizar: "))
    n_dos = float(input("Ingrese el segundo número a analizar: "))
    if n_uno < n_dos:
        n_uno,n_dos = n_dos,n_uno
    if n_dos == n_uno:
        print("Son el mismo número")
    else:
        if primos_relativos(n_uno, n_dos):
            print("Sí son números primos relativos.")
        else:
            print("No son números primos relativos.")

main()