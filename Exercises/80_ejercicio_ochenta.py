def en(c,e):
    i = 0
    flag = False
    while i < len(c) and flag == False:
        if c[i] == e:
            flag = True
        i+=1
    return flag

def decodifique(C,c):
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = ""
    for i in range(len(C)):
        if en(abc,C[i]):
            for n in range(len(abc)):
                if C[i] == c[n]:
                    code += abc[n]
        else:
            code += C[i]
    return code

def main():
    C = input("Ingrese el mensaje cifrado que desea decodificar: ")
    c = input("Ingrese la cadena de correspondencia con la que está cifrado el mensaje (26 letras sin la ñ): ")
    print(decodifique(C,c))

main()