def delete_all(C,c):
    C_f = ""
    for i in range(len(C)):
        if C[i] != c:
            C_f += C[i]
    return C_f

def f_palindrome(C):
    C = delete_all(C," ")
    m = 0
    Flag = True 
    while m < len(C)//2 and Flag: #Mientras m sea menor a la mitad de la cadena
        if C[m] != C[len(C)-1-m]:
            Flag = False
        else:
            m+= 1
    return Flag

def main():
    C = input("Ingrese la frase que desea saber si es palíndorme: ")
    if f_palindrome(C):
        print("La frase que ingresó sí es palíndrome.")
    else:
        print("La frase que ingresó no es palíndrome.")
    
main()