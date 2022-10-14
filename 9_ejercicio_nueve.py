def divisible(N,n_uno,n_dos):
    if N % (n_uno + n_dos) == 0:
        return True

def main():
    N = float(input("Ingrese el número a analizar: "))
    n_uno = float(input("Ingrese el primer dígito de la suma: "))
    n_dos = float(input("Ingrese el segundo dígito de la suma: "))
    if divisible(N,n_uno,n_dos):
        print("El número a analizar es divisible por la suma de los valores registrados.")
    else:
        print("El número a analizar no es divisible por la suma de los valores registrados.")

main()