def elementos(n_d):
    l = []
    for e in range(n_d):
        e = int(input("Ingrese los " + str(n_d) + " coeficientes que acompañan a cada x del polinomio (en orden ascendente comnzando por x elevado a cero): "))
        l.append(e)
    return l

def reverse(l):
    l_f = []
    for i in range(len(l)-1,-1,-1):
        l_f.append(l[i])
    return l_f

def evaluar(p,x):
    r = 0
    for i in range(len(p)):
        r += p[i] * (x ** i)
    return r

def sumar(p_uno,p_dos):
    if len(p_uno) > len(p_dos):
        p_a , p_b = p_uno.copy() , p_dos.copy()
    else:
        p_a , p_b = p_dos.copy() , p_uno.copy()
    for i in range (len(p_b)):
        p_a[i] = p_a[i] + p_b[i]
    return p_a

def restar(p_uno,p_dos):
    if len(p_uno) > len(p_dos):
        p_a , p_b = p_uno.copy() , p_dos.copy()
    else:
        p_a , p_b = p_dos.copy() , p_uno.copy()
    for i in range (len(p_b)):
        p_a[i] = p_a[i] - p_b[i]
    return p_a

def multiplicar(p_uno,p_dos):
    p_m = []
    ceros = []
    for i in range (len(p_dos)):
        p_t = []
        for n in range (len(p_uno)):
            p_t.append(p_uno[n] * p_dos[i])
        p_t = ceros + p_t
        p_m = sumar(p_m,p_t)
        ceros.append(0)    
    return p_m

def dividir(p_uno,p_dos):
    p_a , p_b = reverse(p_uno) , reverse(p_dos)
    p_c = []
    while len(p_a) >= len(p_b):
        l_c = [(p_a[0] // p_b[0])] #Convertir el intento de cociente en arreglo para poder reutilizar función multiplicar. 
        p_c.append(p_a[0] // p_b[0])
        p_r = multiplicar(p_b,l_c) #Polinomio que se le restará al dividiendo (p_a).
        p_a = restar(p_a,p_r)
        while len(p_a) > 0 and p_a[0] == 0: #Quitar ceros a la izquierda que no dañan el while principal
            p_a.pop(0)
    while len(p_uno) - len(p_dos) != len(p_c) - 1: #Añadir ceros a la derecha de ser necesario para conservar el grado del polinomio cociente al ser representado como arreglo.
        p_c.append(0)
    return reverse(p_c),p_a

def dividir_recursiva(p_a,p_b,p_c):
    if len(p_a) < len(p_b):
        return reverse(p_c),p_a
    else:
        l_c = [(p_a[0] // p_b[0])] #Convertir el intento de cociente en arreglo para poder reutilizar función multiplicar. 
        p_c.append(p_a[0] // p_b[0])
        p_r = multiplicar(p_b,l_c) #Polinomio que se le restará al dividiendo (p_a).
        p_a = restar(p_a,p_r)
        while len(p_a) > 0 and p_a[0] == 0: #Quitar ceros a la izquierda que no dañan el condicional
            p_a.pop(0)
        return dividir_recursiva(p_a,p_b,p_c)

def main():
    print("Bienvenido al operador de polinomios.")
    o = int(input("Ingrese la operación que desea realizar (Evaluar = 1, Sumar = 2, Restar = 3, Multiplicar = 4, Dividir = 5, Residuo = 6): "))
    g_uno = int(input("Ahora ingresa el grado del primer polinomio: "))
    g_dos = int(input("Y ahora ingrese el grado del segundo polinomio: "))
    p_uno = elementos(g_uno + 1)
    p_dos = elementos(g_dos + 1)
    while o != 7:
        if o == 1:
            x = float(input("Ingrese el valor de x en el que quiere evaluar los dos polinomios: "))
            print("La evaluación del primer polinomio en la x ingresada es" , evaluar(p_uno,x) , "y en el segundo polinomio es" , evaluar(p_dos,x))
        elif o == 2: 
            print("La suma de los polinomios ingresados es" , sumar(p_uno,p_dos))
        elif o == 3:
            print("La resta del segundo polinomio al primer polinomio ingresado es" , restar(p_uno,p_dos))
        elif o == 4:
            print("La multiplicación de los polinomios ingresados es" , multiplicar(p_uno,p_dos))
        elif o == 5:
            if len(p_uno) < len(p_dos):
                print("Polinomios no válidos para ser divididos.")
            else:
                p_c = []
                p_c,r = dividir(p_uno,p_dos)
                print("La división entre el primer polinomio sobre el segundo polinomio ingresado es" , p_c)
        elif o == 6:
            p_c,r = dividir(p_uno,p_dos)
            print("El residuio de la división entre el primer polinomio sobre el segundo polinomio ingresado es" , r)
        else:
            print("El número de operación ingresado no es válido, intente nuevamente.")     
        o = int(input("Ingrese nuevamente la operación que desea realizar o ingrese 7 para salir (Evaluar = 1, Sumar = 2, Restar = 3, Multiplicar = 4, Dividir = 5, Residuo = 6): "))
    return "Gracias por preferirnos."

main()