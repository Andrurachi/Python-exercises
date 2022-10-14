def producto_recursiva(l_uno,l_dos,p_p,n_d):
    if n_d == 0:
        return p_p
    else:
        p_p += l_uno[n_d-1] * l_dos[n_d-1]
        return producto_recursiva(l_uno,l_dos,p_p,n_d-1)

def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def producto(l_uno,l_dos):
    p_p = 0
    for i in range(len(l_uno)):
        p_p += l_uno[i] * l_dos[i]
    return p_p    

def main():
    n_d = int(input("Ingrese el número total de datos que tendrá cada arreglo para sacarle el producto punto: "))
    l_uno , l_dos = elementos(n_d) , elementos(n_d)
    print("El producto punto de los dos arreglos es:" , producto(l_uno,l_dos)) 

main()