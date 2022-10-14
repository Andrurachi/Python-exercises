def evaluar_en_x(c_uno,c_dos,c_tres,x):
    return c_uno * x ** 2 + c_dos * x + c_tres

def main():
    c_uno = float(input("Ingrese el coeficiente que acompaña al x^2 del polinomio: "))
    c_dos = float(input("Ingrese el coeficiente que acompaña al x del polinomio: "))
    c_tres = float(input("Ingrese el término independiente del polinomio: "))
    x = float(input("Ingrese el valor en el que desea evaluar el polinomio: "))
    print("La evaluación del polinomio en el valor de x es de" , evaluar_en_x(c_uno,c_dos,c_tres,x))

main()