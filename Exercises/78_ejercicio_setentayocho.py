def c_derecha(C):
    C_d = ""
    C_d += C[len(C)-1]
    for i in range (len(C)-1):
        C_d += C[i]
    return C_d

def main():
    C = input("Ingrese la cadena a la que le desea hacer el corrimiento circular a derecha: ")
    print("la cadena es la siguiente:" , c_derecha(C))

main()