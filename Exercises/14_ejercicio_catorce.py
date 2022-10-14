def analiza_rectas():
    m_uno = float(input("Ingrese la pendiente de la primera recta: "))
    m_dos = float(input("Ingrese la pendiente de la segunda recta: "))
    y_uno = float(input("Ingrese el punto de corte en y de la primera recta: "))
    y_dos = float(input("Ingrese el punto de corte en y de la segunda recta: "))
    if m_uno == m_dos and y_uno != y_dos:
        print ("Las rectas registradas son paralelas")
    elif m_uno == m_dos and y_uno == y_dos:
        print("Las rectas registradas tienen la misma imagen en la gráfica")
    elif m_uno * m_dos == -1:
        print("Las rectas registradas son perpendiculares")
    else:
        print("Las rectas registradas no son ni paralelas ni perpendiculares")

analiza_rectas()