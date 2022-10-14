def puntos_inter(m_uno,m_dos,y_uno,y_dos):
        x = (y_dos - y_uno) / (m_uno - m_dos)
        y = m_uno * x + y_uno
        return x,y

def diferentes(m_uno,m_dos):
    if m_uno != m_dos:
        return True

def main():
    m_uno = float(input("Ingrese la pendiente de la primera recta: "))
    m_dos = float(input("Ingrese la pendiente de la segunda recta: "))
    y_uno = float(input("Ingrese el punto de intersección con el eje Y de la primera recta: "))
    y_dos = float(input("Ingrese el punto de intersección con el eje Y de la segunda recta: "))
    if diferentes(m_uno,m_dos):
        print("El punto de intersección de las rectas ocurre en las coordenadas" , puntos_inter(m_uno, m_dos, y_uno, y_dos))
    else:
        print("Las rectas ingresadas o son paralelas o son la misma por lo que no tienen intersección")

main()