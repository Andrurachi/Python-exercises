def primos_recursiva(num,i):
    if i == num:
        return True
    elif num % i == 0:
        return False
    else:
        return (primos_recursiva(num,i+1))

def primos(num):
    i = 2
    flag = True
    while i < num and flag:
        if num % i == 0: 
            flag = False
        i += 1
    return flag

def main():
    num = int(input("Ingrese el número a analizar: "))
    if num <= 0:
        print("No es número primo porque es negativo o cero. Ingrese nuevamente el número pero con signo positivo o diferente a cero")
        main()
    elif primos(num):
        print("Sí es un número primo.")
    else:
       print("No es un número primo.")

main()