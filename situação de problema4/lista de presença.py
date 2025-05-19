pais_presentes = []
pais_ausentes = []
nomes_pais = []
while True:
    print("menu da reunião de pais ")
    print("[1] - cadastrar nome ")
    print("[2] - exibir o total de pais ")
    print("[3] - exibir a lista de nomes em ordem alfabética ")
    print("[4] - realizar a confirmação de presença dos pais ")
    print("[5] - exibir um relatório da chamada")
   
    num = input("digite um numero de 1 ao 5 = ")
    if num == "1":
        nome = input("digite seu nome ")
        if nome in nomes_pais:
            print("este nome já está na lista ")
        else:
            nomes_pais.append(nome)
            print("nome adicionado ")
    elif num == "2":
        print("a quantidade de pais é ", len(nomes_pais))
       
    elif num == "3":
        nomes_pais.sort()
        print("lista dos nomes dos pais  ")
        for nome in nomes_pais:
            print(nome)
           
    elif num == "4":
        for nome in nomes_pais:
            print(nome)
            nome_consulta = input("está presente? (s/n) ")
            if nome_consulta == "s":
                pais_presentes.append(nome)
                print("pai presente ")
            else:
               pais_ausentes.append(nome)
               print("pai ausente ")
   
    elif num == "5":
        print("pais presentes ")
        for nome in pais_presentes:
            print(nome)
        print("pais ausentes ")
        for nome in pais_ausentes:
            print(nome)
        
        