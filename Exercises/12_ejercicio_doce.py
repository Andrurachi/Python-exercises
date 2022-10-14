def eva_derivada(c_uno,c_dos,x):
    return (c_uno * 2 * x) + c_dos 

def main():
    c_uno = float(input("Ingrese el coeficiente que acompaña al x^2 del polinomio: "))
    c_dos = float(input("Ingrese el coeficiente que acompaña al x del polinomio: "))
    c_tres = float(input("Ingrese el término independiente del polinomio: "))
    x = float(input("Ingrese el valor en el que desea evaluar el polinomio: "))
    print("La evalución de la derivada del polinomio de segundo grado en" ,  x , "es" , eva_derivada(c_uno,c_dos,x)) 

main()