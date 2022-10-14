def c_izquierda(C):
    C_i = ""
    C += C[0]
    for i in range (1,len(C)):
        C_i += C[i]
    return C_i

def main():
    C = input("Ingrese la cadena a la que le desea hacer el corrimiento circular a izquierda: ")
    print("la cadena es la siguiente:",c_izquierda(C))

main()