def area_triangulo(r):
    a_t = 3 * 1.73205080757 * (r ** 2)
    return a_t

def main():
    r = float(input("Ingrese el radio de la circunferencia inscrita en el triángulo equilátero en cm: "))
    print("El área de el triángulo equilátero en el que se encuentra inscrito la circunferencia de radio " , r , " es de" , area_triangulo(r) , "cm^2")

main()