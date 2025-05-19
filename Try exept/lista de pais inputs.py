import inputs
nomes_pais = []
pais_ausentes = []
pais_presentes = []
while True:
    print("menu da reunião de pais ")
    print("[1] - cadastrar nome ")
    print("[2] - exibir o total de pais ")
    print("[3] - exibir a lista de nomes em ordem alfabética ")
    print("[4] - realizar a confirmação de presença dos pais ")
    print("[5] - exibir um relatório da chamada")
   
    escolha = inputs.input_int(("escolha uma opção "))
    if escolha == 1:
        nome = inputs.input_str("escreva seu nome ")
        if nome in nomes_pais:
            print("este nome já está na lista ")
        else:
            nomes_pais.append(nome)
            print("nome adicionado ")
    elif escolha == 2:
        print("a quantidade de pais é ", len(nomes_pais))
       
    elif escolha == 3:
        nomes_pais.sort()
        print("lista dos nomes dos pais  ")
        for nome in nomes_pais:
            print(nome)
           
    elif escolha == 4:
        for nome in nomes_pais:
            print(nome)
            nome_consulta = inputs.input_str("está presente? (s/n) ")
            if nome_consulta == "s":
                pais_presentes.append(nome)
                print("pai presente ")
            else:
               pais_ausentes.append(nome)
               print("pai ausente ")
   
    elif escolha == 5:
        print("pais presentes ")
        for nome in pais_presentes:
            print(nome)
            print("")
        print("pais ausentes ")
        for nome in pais_ausentes:
            print(nome)
            print("")

   
   
         