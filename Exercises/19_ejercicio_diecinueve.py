def n_arboles_recursiva(a,h_count,h_a,o_h):
    if h_count >= o_h:
        return a
    else:
        return n_arboles_recursiva(a+1,h_count+h_a,h_a,o_h)

def n_arboles(h_r,r_a,o_h):
    a = 0 #Árboles
    h_count = 0 #Contador de hojas
    h_a = r_a * h_r  #Hojas por árbol
    while o_h > h_count:
        h_count += h_a
        a += 1
    return a

def main():
    h_r = int(input("Ingrese el número de hojas por rama: "))
    r_a = int(input("Ingrese el número de ramas por arbol: "))
    o_h = int(input("Ingrese el número total de hojas que desean quitar: "))
    print("El número mínimo de arboles que se deben talar es de" , n_arboles(h_r,r_a,o_h))

main()