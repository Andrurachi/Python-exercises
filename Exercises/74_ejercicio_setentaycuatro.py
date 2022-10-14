def reverse(C):
    C_f = ""
    for i in range(len(C)-1,-1,-1):
        C_f += (C[i])
    return C_f

def main():
    C = input("Ingrese la cadena de carácteres que desea invertir: ")
    print("La cadena que ingreso invertida es: ", reverse(C))

main()