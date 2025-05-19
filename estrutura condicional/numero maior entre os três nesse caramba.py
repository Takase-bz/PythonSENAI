print("solicite 3 Numeros para comparalos:")
x1 = int(input("1ºNumero: "))
x2 = int(input("2ºNumero: "))
x3 = int(input("3ºNumero: "))

if x1 > x2:
    if x1 > x3:
        print("Numero 1 é o maior")

if x2 > x3:
    if x2 > x1:
        print("Numero 2 é o maior")

if x3 > x1:
    if x3 > x2:
        print("Numero 3 é o maior")
        
        