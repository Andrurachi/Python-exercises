def en(c,e):
    i = 0
    flag = False
    while i < len(c) and flag == False:
        if c[i] == e:
            flag = True
        i+=1
    return flag

def codifique(C,c):
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = ""
    for i in range (len(C)):
        if en(abc,C[i]):
            for n in range (len(abc)):
                if C[i] == abc[n]:
                    code += c[n]
        else:
            code += C[i]
    return code


def codifique_2(C,c):
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = ""
    for i in range (len(C)):
        if en(abc,C[i]):
            for n in range(len(abc)):
                if C[i] == abc[n]:
                    if len(c) > n:
                        code += c[n]
                    else:
                        code += C[i]
        else:
            code += C[i]
    return code

def main():
    C = input("Ingrese la cadena que desea codificar: ")
    c = input("Ingrese la cadena de correspondencia con la que desea codificar (26 letras sin la ñ): ")
    print(codifique(C,c))

main()
