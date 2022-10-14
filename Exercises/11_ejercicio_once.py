def dev_lineal(c_uno):
    return c_uno * 2

def main():
    c_uno = float(input("Ingrese el coeficiente que acompaña al x^2 del polinomio: "))
    c_dos = float(input("Ingrese el coeficiente que acompaña al x del polinomio: "))
    c_tres = float(input("Ingrese el término independiente del polinomio: "))
    print("La derivada lineal del polinomio es:" , dev_lineal(c_uno))

main()    