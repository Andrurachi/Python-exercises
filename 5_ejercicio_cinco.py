def potencia_recursiva(b,e):
    if e == 0:
        return 1
    elif e > 0:
        return potencia_recursiva(b,e-1) * b
    elif e < 0:
        return potencia_recursiva(b,e+1) * b

def potencia(b,e):
    r = 1
    if e >= 0:
        while e > 0:       
            r = r * b
            e -= 1
    elif e < 0:
        while e < 0:       
            r = r * b
            e += 1
        r = 1/r
    return r

def main():
    b = int(input("Ingrese la base de de la potenciación para su función (número entero): "))
    e = int(input("Ingrese el exponente de la potenciación para su función (número entero): "))
    
    if e <= 0 and b == 0:
        print("Error, potencia inválida.")   
    else:
        print("El resultado de tu pontencia es " , potencia(b,e))
        if e < 0:
            print("El resultado de tu pontencia es " , 1 / potencia_recursiva(b,e))
        else:
            print("El resultado de tu pontencia es " , potencia_recursiva(b,e))

main()
