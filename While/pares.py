numero = int(input("solicite o numero"))
quantidade = 0
while True:
    numero= numero - 1
    if numero % 2 == 1:
        print(numero)
        quantidade = quantidade + 1
        
        
    elif numero <= 0:
        print("a quantidade de numeros pares é", quantidade)
        break 