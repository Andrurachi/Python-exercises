def reverse(C):
    C_f = ""
    for i in range(len(C)-1,-1,-1):
        C_f += (C[i])
    return C_f

def c_palindrome(C):
    C_i = reverse(C)
    if C == C_i:
        return True

def main():
    C = input("Ingrese la cadena que desea saber si es palíndorme: ")
    if c_palindrome(C):
        print("La cadena que ingresó sí es palíndrome.")
    else:
        print("La cadena que ingresó no es palíndrome.")

main()