def i_simple(p,i):
    i_s = i * 7 #Interés por semana
    return p + i_s

def i_compuesto(p,i):
    return p * (( 1 + (i/p)) ** 7)

def main():
    p = int(input("Ingrese la cantidad de pesos que le prestaron: "))
    i = int(input("ingrese los pesos diarios de interés a los que le prestaron: "))
    print("El valor a pagar con interés simple es de" , i_simple(p,i) , "y con interés compuesto es de" , i_compuesto(p,i))

main()