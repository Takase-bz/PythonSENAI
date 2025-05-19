
nomes = []
while True:
    
    
    
    print("")
    print("[1] cadastrar nome")
    print("[2] exibir o total de inscritos")
    print("[3] exibir a lista de nomes em ordem alfabetica")
    print("[4] permitir a consulta de um nome")
    print("[5] sair")
    num = input("digite um numero de 1 a 5")
    
    
    if num == "1":
        nomee = input("digite o seu nome")
    
        print(nomee)
        if nomee in nomes:
            print("nome encontrado")
        else:
            nomes.append(nomee)
            
    elif num == "2":
        print(len(nomes))
        
        
    elif num == "3":
        print("lista de inscritos")
        nomes.sort()
        for nome in nomes:
        
            print(nome)
    elif num == "4":
        nome = input("digite o seu nome")
    
        if nome in nomes:
            print("nome encontrado")
            print("deseja remover o nome")
            print("s")
            print("n")
            num2 = input("numero de 1 a 2")
            if num2 == "s":
                nomes.remove(nome)
            else:
                print("ok")
        else:
            print("nome não encontrado")
            print("deseja adicionar")
            print("s")
            print("n")
            num2 = input(" s ou n")
            
            if num2 == "s":
                nome = input("digite o seu nome")
                nomes.append(nome)
                    
                    
                    
    elif num == "5":
        print("sair")
        break
            





        
