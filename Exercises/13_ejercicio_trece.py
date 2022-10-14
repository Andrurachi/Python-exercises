def fibonacci_recursivo(num,f_i,f_f):
    if f_i + f_f > num:
        return False
    elif f_i + f_f == num:
        return True
    else:
        return fibonacci_recursivo(num,f_f,f_i + f_f)

def fibonacci(num):
    flag = False
    F = 0 #Intento de fabonacci
    f_i = 0 #Donde se conservará el penúltimo intento de fabonacci para crear un nuevo intento de fabonacci
    f_f = 1 #Donde se conservará el último intento de fabonacci para crear un nuevo intento de fabonacci
    while num >= F and flag == False:
        if num == F:
            flag = True
        F = f_i + f_f
        f_i = f_f
        f_f = F
    return flag

def main():
    num = int(input("Ingrese un número natural a evaluar: "))
    if fibonacci(num):
        print("El número ingresado sí es un número de Fibonacci. ")
    else:
        print("El número ingresado no es un número de Fibonacci. ")

main()