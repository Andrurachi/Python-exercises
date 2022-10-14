def listado_recursiva(num,l):
    if num < 2:
        return l[::-1]
    else:
        if primos(num):
            l.append(num)
        return listado_recursiva(num-1,l)

def primos(num):
    flag = True
    i = 2
    while i < num and flag:
        if num % i == 0:
            flag = False
        i += 1
    return flag

def listado(num):
    l = []
    for num in range(2,num+1):
        if primos(num):
            l.append(num)
    return l

def main():
    num = int(input("Ingrese el número del que quiere conocer los primos que le preceden: ")) -1
    l = []
    print("La lista de los números primos anteriores al ingresado es (evaluando el ingreesado): " , listado(num))

main()