def delete(C,c):
    C_f = "" 
    flag = True
    for i in range(len(C)):
        if C[i] == c and flag:
            flag = False
        else:
            C_f += C[i]
    return C_f

def en(c,e):
    i = 0
    flag = False
    while i < len(c) and flag == False:
        if c[i] == e:
            flag = True
        i+=1
    return flag

def incluida(C_uno,C_dos):
    flag = True
    i = 0
    while i < len(C_uno) and flag:
        if en(C_dos,C_uno[i]):
            C_dos = delete(C_dos,C_uno[i])
            i+=1
        else:
            flag = False
    return flag

def main():
    C_uno = str(input("Ingrese la primera cadena de caracteres: "))
    C_dos = str(input("Ingrese la segunda cadena de caracteres: "))
    if incluida(C_uno,C_dos):
        print("La primera cadena sí está incluida en la segunda.")
    else:
        print("La primera cadena no está incluida en la segunda." )

main()