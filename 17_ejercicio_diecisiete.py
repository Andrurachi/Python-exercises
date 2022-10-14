def a_cuadrado_i(radio):
    area = 4 * (radio * radio / 2)
    return area

def a_hexagono_i(radio):
    area = 12 * ((0.5 * radio) * (0.8660254038 * radio) / 2)
    return area

def a_pentagono_i(radio):
    area = 10 * ((0.5877852523 * radio) * (0.8090169944 * radio) / 2)
    return area

def p_cuadrado_i(radio):
    perimetro = 8 * (0.7071067812 * radio)
    return perimetro

def p_hexagono_i(radio):
    perimetro = 12 * (0.5 * radio)
    return perimetro
    
def p_pentagono_i(radio):
    perimetro = 10 * (0.5877852523 * radio)
    return perimetro

def a_cuadrado_e(radio):
    area = 4 * (radio * radio)
    return area

def a_hexagono_e(radio):
    area = 12 * ((0.5 * radio / 0.8660254038) * radio / 2)
    return area

def a_pentagono_e(radio):
    area = 10 * ((0.5877852523 * radio / 0.8090169944) * radio / 2)
    return area

def p_cuadrado_e(radio):
    perimetro = 8 * (radio)
    return perimetro

def p_hexagono_e(radio):
    perimetro = 12 * (0.5 * radio / 0.8660254038)
    return perimetro
    
def p_pentagono_e(radio):
    perimetro = 10 * (0.5877852523 * radio / 0.8090169944)
    return perimetro

def main():
    radio = float(input("Ingrese el radio de su circunferencia: "))
    print("El area del cuadrado, hexágono y pentágono graficado dentro de su circunferencia son respectivamente: " + str(a_cuadrado_i(radio)) + ",  "  + str(a_hexagono_i(radio))+ ",  "  + str(a_pentagono_i(radio)))
    print("El area del cuadrado, hexágono y pentágono graficado fuera de su circunferencia son respectivamente: " + str(a_cuadrado_e(radio)) + ",  "  + str(a_hexagono_e(radio)) + ",  " + str(a_pentagono_e(radio)))
    print("El perímetro del cuadrado, hexágono y pentágono graficado dentro de su circunferencia son respectivamente: " + str(p_cuadrado_i(radio)) + ",  "  + str(p_hexagono_i(radio)) + ",  "  + str(p_pentagono_i(radio)))
    print("El area del cuadrado, hexágono y pentágono graficado fuera de su circunferencia son respectivamente: " +  str(p_cuadrado_e(radio)) + ",  " + str(p_hexagono_e(radio)) + ",  "  + str(p_pentagono_e(radio)))

main()