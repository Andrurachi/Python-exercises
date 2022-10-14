def contar(C,c):
    count = 0
    for i in range (len(C)):
        if C[i] == c:
            count += 1
    return count

def main():
    C = str(input("Ingrese el caractér que desea buscar: "))
    c = str(input("Ingrese la cadena de caracteres: "))
    print("El número de veces que el caractér está en la cadena es: " , contar(C,c))

main()