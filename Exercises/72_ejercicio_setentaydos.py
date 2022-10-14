def subcadena(C_uno,C_dos):
    flag = False
    t = 0
    while len(C_uno)+t <= len(C_dos) and flag == False:
        C_i = ""
        for i in range(t,t+len(C_uno)):
            C_i += C_dos[i]
        if C_i == C_uno:
            flag = True
        t += 1
    return flag

def main():
    C_uno = str(input("Ingrese la primera cadena de caracteres: "))
    C_dos = str(input("Ingrese la segunda cadena de caracteres: "))
    if subcadena(C_uno,C_dos):
        print("La primera cadena de carácteres sí es subcadena de la segunda cadena.")
    else:
        print("La primera cadena de carácteres no es subcadena de la segunda cadena.")

main()
