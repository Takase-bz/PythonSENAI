while True:
    print("Defina dois numeros para efetuar contas basicas")
    print("")
    print("[1] fatorial")
    print("[2] quadrado")
    print("[3] cubo")
    print("[4] tabuada")
    print("[0] sair")
    num = input("Numero de [0-4]: ")
    print("")
    
    
    
    if num == "1":
        numero = int(input("Fatorial de: ") )

        resultado=1
        count=1

        while count <= numero:
            resultado *= count
            count += 1

        print(resultado)
    
    
    elif num == "2":
        lado = int(input("solicite o valor do lado"))
        conta1 = pow(lado, 2)
        print(conta1)
    elif num == "3":
        lado2 = int(input("solicite o valor do lado"))
        conta2 = pow(lado2, 3)
        print(conta2)
    elif num == "4":
        t = int(input("Número"))
        print("Tabuada do", t)
        print(t, 'x 1 =', t * 1)
        print(t, 'x 2 =', t * 2)
        print(t, 'x 3 =', t * 3)
        print(t, 'x 4 =', t * 4)
        print(t, 'x 5 =', t * 5)
        print(t, 'x 6 =', t * 6)
        print(t, 'x 7 =', t * 7)
        print(t, 'x 8 =', t * 8)
        print(t, 'x 9 =', t * 9)
        print(t, 'x 10 =', t * 10)
    
    
    
    
    elif num == "0":
        print("Sair")
        break
    
        
    