def reverse(l):
    l_f = []
    for i in range(len(l)-1,-1,-1):
        l_f.append(l[i])
    return l_f

def binario(d):
    b = []
    while d >= 1:
        b.append(d % 2) 
        d //= 2
    return reverse(b)
    
def main():
    d = int(input("Ingrese el número entero no negativo que desea convertir a binario: "))
    print("El número en binario es " , binario(d))

main()