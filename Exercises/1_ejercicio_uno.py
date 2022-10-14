def leche(p,a,m_l):   
    return p * a / m_l

def main():
    p = float(input("Digite la profundidad de su granja: "))
    a = float(input("Digite el ancho de su granja: "))
    m_l = float(input("Digite el número de metros cuadrados que una vaca necesita para producir un litro de leche: "))
    print("La cantidad en litros de leche que las dimensiones de su granja le permiten producir es de " , leche(p,a,m_l) , " litros")
 
main()