def kilos_venta_recursivo(e_20,e_30,e_50,e_v):
    if e_v == 0:
        return 0
    elif e_50 > 0:
        return kilos_venta_recursivo(e_20,e_30,e_50-1,e_v-1) + 50
    elif e_30 > 0:
        return kilos_venta_recursivo(e_20,e_30-1,e_50,e_v-1) + 30
    elif e_20 > 0:
        return kilos_venta_recursivo(e_20-1,e_30,e_50-1,e_v-1) + 20 

def kilos_venta(e_20,e_30,e_50,e_100):
    e_v = (e_20 + e_30 + e_50 + e_100) // 3 
    gr_t = 0
    while e_v > 0:
        while e_100 > 0 and e_v > 0:
            gr_t += 100
            e_100 -= 1
            e_v -= 1
        while e_50 > 0 and e_v > 0:
            gr_t += 50
            e_50 -= 1
            e_v -= 1
        while e_30 > 0 and e_v> 0:
            gr_t += 30
            e_30 -= 1
            e_v -= 1
        while e_20 > 0 and e_v > 0:
            gr_t += 20
            e_20 -= 1
            e_v -= 1
    return gr_t / 1000
    
def main():
    e_20 = int(input("Ingrese el número de escorpiones que posee de tamaño pequeño: "))
    e_30 = int(input("Ingrese el número de escorpiones que posee de tamaño mediano: "))
    e_50 = int(input("Ingrese el número de escorpiones que posee de tamaño grande: "))
    print("El peso máxima de escorpiones que puede vender sin reducir su población a menos de dos tercios es de" , kilos_venta(e_20, e_30, e_50) , "kg")
    e_v = (e_20 + e_30 + e_50) // 3
    print("El peso máxima de escorpiones que puede vender sin reducir su población a menos de dos tercios es de" , (kilos_venta_recursivo(e_20, e_30, e_50,e_v) / 1000) , "kg")

main()