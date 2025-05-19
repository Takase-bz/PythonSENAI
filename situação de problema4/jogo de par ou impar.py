import random



while True:
    print("PAR OU IMPAR")
    print("")
    print("[1] Par")
    print("[2] Impar")
    print("[0] Sair")
    num = input("Numero de [0-2]: ")
    print("")
    
    if num == "1":
        n_aleatorio = random.randint(0,10)
        n_jogador = int(input("digite seu numero"))
        numero = n_aleatorio + n_jogador
        print("eu escolhi", n_aleatorio)
        if numero % 2 == 0:
            print(numero, "você ganhou!")
        elif numero % 2 == 1:
            print(numero, "você perdeu, tente novamente")
            
        
    elif num == "2":
        n_aleatorio = random.randint(0,10)
        n_jogador = int(input("digite seu numero"))
        numero = n_aleatorio + n_jogador
        print("eu escolhi", n_aleatorio)
        if numero % 2 == 0:
                    print(numero, "você perdeu, tente novamente")
        elif numero % 2 == 1:
                    print(numero, "você ganhou!")
                    
                    
    else:
        "0"
        print("Sair")
        break
                
            
        
                
    
        
        
        


    




    