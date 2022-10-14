def producto_directo_recursiva(l_uno,l_dos,p_d,n_d):
    if n_d == 0:
        return p_d
    else:
        p_d.append(l_uno[len(l_uno)-n_d] * l_dos[len(l_uno)-n_d])
        return producto_directo_recursiva(l_uno,l_dos,p_d,n_d-1)

def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " elementos del arreglo: "))
        l.append(e)
    return l

def producto_directo(l_uno,l_dos):
    p_d = []
    for i in range(len(l_uno)):
        p_d.append(l_uno[i]*l_dos[i])
    return p_d

def main():
    n_d = int(input("Ingrese el número total de datos que tendrá cada arreglo para sacarle el producto directo: "))
    l_uno , l_dos = elementos(n_d) , elementos(n_d)
    p_d = []
    print("El prodcuto directo de los dos arreglos es:" , producto_directo(l_uno,l_dos)) 

main()