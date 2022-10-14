def divisible(D,d):
    if D % d == 0:
        return True
    
def main():
    D = float(input("Ingrese el dividiendo que desee: "))
    d = float(input("Ingrese el divisor que desee: "))
    if divisible(D,d):
        print("El dividiendo sí es divisible.")
    else:
        print("El dividiendo no es divisible.")

main()