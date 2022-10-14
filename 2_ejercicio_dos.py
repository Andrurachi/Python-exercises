def huevos(a):
    h_t = int(a / 3 / 2 * 10 + a / 3 / 2 * 6)
    return h_t

def main():
    a = int(input("Ingrese el número de aves que posee: "))
    while a % 6 != 0:
        a = int(input("Error, el número no es divisible en 6. Ingrese nuevamente el número: "))
    print("La cantidad de huevos que producen tus gallinas es de " , huevos(a)) 

main()