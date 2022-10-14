def telaraña_recursiva(r,R):
    if r == 0:
        return 6 * R
    else:
        return telaraña_recursiva(r-1,R) + 6 * r

def telaraña(r):
    p = 6 * r
    while r > 0:
        p += 6 * r
        r -= 1
    return p 

def main():
    r = int(input("Ingrese el radio de la telaraña en centímetros: "))
    print("La cantidad de telaraña en centímetros que requiere la araña es de: " , telaraña(r))

main()